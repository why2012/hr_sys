from django.shortcuts import render
from hr_sys.decorators import checklogin
from hr_sys.models import UserGroup, User, MenuItem, UserGroupMenuItem
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

@checklogin()
def index(request):
    context = {}
    userid = request.session["userid"]
    currUser = User.objects.get(pk=userid)
    currUserGroup = currUser.user_group
    userGroupMenuItems = UserGroupMenuItem.objects.filter(user_group_id=currUserGroup.id)
    menuTree = {}
    parentMenuItemOrdering = []
    for groupMenuItem in userGroupMenuItems:
        menuItem = groupMenuItem.menu_item
        if menuItem.type == 0:
            if menuItem.id not in menuTree:
                menuTree[menuItem.id] = {"name": menuItem.name, "order": menuItem.order, "childIds": [], "childDetail": []}
            if menuItem.id in menuTree and (menuTree[menuItem.id]["name"] is None or menuTree[menuItem.id]["order"] is None):
                menuTree[menuItem.id]["name"] = menuItem.name
                menuTree[menuItem.id]["order"] = menuItem.order
            currChildMenuItems = MenuItem.objects.filter(parent_id=menuItem.id)
            for tmpMenuItem in currChildMenuItems:
                if tmpMenuItem.id not in menuTree[menuItem.id]["childIds"]:
                    menuTree[menuItem.id]["childDetail"].append(tmpMenuItem);
        else:
            if menuItem.parent_id != -1 and menuItem.parent_id not in menuTree:
                menuTree[menuItem.parent_id] = {"name": None, "order": None, "childIds": [], "childDetail": []}
            if menuItem.id not in menuTree[menuItem.parent_id]["childIds"]:
                menuTree[menuItem.parent_id]["childDetail"].append(menuItem)
    for parentMenuItemId, data in menuTree.items():
        if data["name"] is None or data["order"] is None:
            parentMenuItem = MenuItem.objects.get(pk=parentMenuItemId)
            data["name"] = parentMenuItem.name
            data["order"] = parentMenuItem.order
        data["childIds"].sort(key=lambda item: item.order)
        parentMenuItemOrdering.append({"id": parentMenuItemId, "order": data["order"]})
    parentMenuItemOrdering.sort(key=lambda item: item["order"])

    orderMenuTree = []
    for parentMenuItemRef in parentMenuItemOrdering:
        parentMenuItem = menuTree[parentMenuItemRef["id"]]
        orderMenuTree.append(parentMenuItem)
    context["orderMenuTree"] = orderMenuTree
    context["username"] = currUser.name

    return render(request, 'main_frame.html', context)

@checklogin()
def overview(request):
    return HttpResponse("Overview")