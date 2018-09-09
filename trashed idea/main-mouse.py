from Cocoa import *
import time
from Foundation import *
from PyObjCTools import AppHelper
from objc import NULL
from Quartz.CoreGraphics import CGEventCreate, CGEventCreateMouseEvent, \
    CGEventGetLocation, CGEventPost, CGEventSetFlags, CGEventSetIntegerValueField,   \
    CGEventSourceCreate, CGPointMake, kCGEventFlagMaskAlternate,                     \
    kCGEventFlagMaskCommand, kCGEventFlagMaskControl, kCGEventFlagMaskShift,         \
    kCGEventLeftMouseDown, kCGEventLeftMouseUp, kCGEventMouseMoved,                  \
    kCGEventRightMouseDown, kCGEventRightMouseUp, kCGEventSourceStateHIDSystemState, \
    kCGHIDEventTap, kCGMouseEventClickState, CGEventGetType, CGEventTapCreate,       \
    kCGHeadInsertEventTap, kCGEventTapOptionListenOnly, CGEventMaskBit
from AppKit import NSEvent, NSScreen, NSPointInRect
from sys import exit


def getMouseLoc():
    mouseEvent = CGEventCreate(NULL)
    mouseLoc = CGEventGetLocation(mouseEvent)
    return mouseLoc


def mouseLocation(isTopCoordinates = True):
    if (isTopCoordinates):
        mLoc = getMouseLoc()
        return (mLoc.x,mLoc.y)
    else:
        mLoc = NSEvent.mouseLocation()
        return (mLoc.x,mLoc.y)


def main():
    returnMouseInfo()


def returnMouseInfo():
    while 1:
        print(mouseLocation())
        pass

main()
