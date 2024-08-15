#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on March 26, 2024, at 01:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""

# --- Import packages ---
import shutil
import csv
import psychopy.event
import numpy
import random, xlrd, time, math
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Behavioural_Test'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    #'PROLIFICID': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
fields = ['Format','stimuli_pair1', 'stimuli_pair2', 'correct_key','key_symbolic_SD.keys', 	'key_symbolic_SD.corr','key_symbolic_SD.rt',
        'image_Nonsymbolic_SD_pair1.started', 'participant', 'psychopyVersion', 'date','expName', 'frameRate']
with open(filename, 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\easpace\\Downloads\Proj2\Proj2_pilot.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
WelcomeScreen = visual.TextStim(win=win, name='WelcomeScreen',
    text='Indicate which is larger using the left < and right > arrow keys \n \n Press SPACEBAR to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_key_resp = keyboard.Keyboard()

Sec1Screen = visual.TextStim(win=win, name='Sec1Screen',
    text='Feel free to rest! \n \n Press SPACEBAR to  continue',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sec1_key_resp = keyboard.Keyboard()

Nonsymbolic_DD_files_original = ['Nonsymbolic_DD_A.csv','Nonsymbolic_DD_B.csv','Nonsymbolic_DD_C.csv','Nonsymbolic_DD_D.csv']
#creates shuffled list of stimuli file
Nonsymbolic_DD_files = Nonsymbolic_DD_files_original
shuffle(Nonsymbolic_DD_files)
print(Nonsymbolic_DD_files)

# --- Initialize components for Routine "select_stimuli_list_SD" ---
# Run 'Begin Experiment' code from code_select_stimuli_SD
Nonsymbolic_SD_curr = -1

# --- Initialize components for Routine "NonSymbolic_SD" ---
image_Nonsymbolic_SD = visual.ImageStim(
    win=win,
    name='image_SD', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_nonsymbolic_SD = keyboard.Keyboard()

image_Nonsymbolic_SD_pair1 = visual.ImageStim(
    win=win,
    name='image_SD_pair1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5,0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_Nonsymbolic_SD_pair2 = visual.ImageStim(
    win=win,
    name='image_SD_pair2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(+0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_nonsymbolic_DD = keyboard.Keyboard()

# --- Initialize components for Routine "Symbolic_SD" ---
text_Symbolic_SD_pair1 = visual.TextStim(win=win, name='text_Symbolic_SD_pair1',
    text='',
    font='Open Sans',
    pos=(-0.5, 0), height=0.25, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_Symbolic_SD_pair2 = visual.TextStim(win=win, name='text_Symbolic_SD_pair2',
    text='',
    font='Open Sans',
    pos=(0.5, 0), height=0.25, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_symbolic_SD = keyboard.Keyboard()

# --- Initialize components for Routine "ExitScreen" ---
text = visual.TextStim(win=win, name='text',
    text="Thanks for participating! \n\nPress 'SPACEBAR' to exit the experiment",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_key_resp.keys = []
welcome_key_resp.rt = []
_welcome_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [WelcomeScreen, welcome_key_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeScreen* updates
    if WelcomeScreen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeScreen.frameNStart = frameN  # exact frame index
        WelcomeScreen.tStart = t  # local t and not account for scr refresh
        WelcomeScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeScreen, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'WelcomeScreen.started')
        WelcomeScreen.setAutoDraw(True)
#    if WelcomeScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
 #       if tThisFlipGlobal > WelcomeScreen.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
 #           WelcomeScreen.tStop = t  # not accounting for scr refresh
 #           WelcomeScreen.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
 #           thisExp.timestampOnFlip(win, 'WelcomeScreen.stopped')
 #           WelcomeScreen.setAutoDraw(False)
    
    # *welcome_key_resp* updates
    waitOnFlip = False
    if welcome_key_resp.status == NOT_STARTED: #and tThisFlip >= resources.status == FINISHED-frameTolerance:
        # keep track of start time/frame for later
        welcome_key_resp.frameNStart = frameN  # exact frame index
        welcome_key_resp.tStart = t  # local t and not account for scr refresh
        welcome_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_key_resp.started')
        welcome_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
#    if welcome_key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
#        if tThisFlipGlobal > welcome_key_resp.tStartRefresh + 20-frameTolerance:
#            # keep track of stop time/frame for later
#            welcome_key_resp.tStop = t  # not accounting for scr refresh
#            welcome_key_resp.frameNStop = frameN  # exact frame index
#            # add timestamp to datafile
#            thisExp.timestampOnFlip(win, 'welcome_key_resp.stopped')
#            welcome_key_resp.status = FINISHED
    if welcome_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _welcome_key_resp_allKeys.extend(theseKeys)
        if len(_welcome_key_resp_allKeys):
            welcome_key_resp.keys = _welcome_key_resp_allKeys[-1].name  # just the last key pressed
            welcome_key_resp.rt = _welcome_key_resp_allKeys[-1].rt
            continueRoutine = False
            # a response ends the routine

    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#check responses
if welcome_key_resp.keys in ['', [], None]:  # No response was made
    welcome_key_resp.keys = None
thisExp.addData('welcome_key_resp.keys',welcome_key_resp.keys)
if welcome_key_resp.keys != None:  # we had a response
    thisExp.addData('welcome_key_resp.rt', welcome_key_resp.rt)
thisExp.nextEntry()
#the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_randomizer = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Block_Randomizer.xlsx'),
    seed=None, name='block_randomizer')
thisExp.addLoop(block_randomizer)  # add the loop to the experiment
thisBlock_randomizer = block_randomizer.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_randomizer.rgb)
if thisBlock_randomizer != None:
    for paramName in thisBlock_randomizer:
        exec('{} = thisBlock_randomizer[paramName]'.format(paramName))

for thisBlock_randomizer in block_randomizer:
    currentLoop = block_randomizer
    #abbreviate parameter names if possible (e.g. rgb = thisBlock_randomizer.rgb)
    if thisBlock_randomizer != None:
        for paramName in thisBlock_randomizer:
            exec('{} = thisBlock_randomizer[paramName]'.format(paramName))
    # --- Prepare to start Routine "load_stimuli_lists" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    load_stimuli_listsComponents = []
    for thisComponent in load_stimuli_listsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "load_stimuli_lists" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in load_stimuli_listsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "load_stimuli_lists" ---
    for thisComponent in load_stimuli_listsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "load_stimuli_lists" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
# set up handler to look after randomisation of conditions etc
    trials_Symbolic_SD = data.TrialHandler(nReps=nReps_symbolic, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Symbolic_pilot.csv'),
        seed=None, name='trials_Symbolic_SD')
    thisExp.addLoop(trials_Symbolic_SD)  # add the loop to the experiment
    thisTrials_Symbolic_SD = trials_Symbolic_SD.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Symbolic_SD.rgb)
    if thisTrials_Symbolic_SD != None:
        for paramName in thisTrials_Symbolic_SD:
            exec('{} = thisTrials_Symbolic_SD[paramName]'.format(paramName))
    
    for thisTrials_Symbolic_SD in trials_Symbolic_SD:
        currentLoop = trials_Symbolic_SD
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Symbolic_SD.rgb)
        if thisTrials_Symbolic_SD != None:
            for paramName in thisTrials_Symbolic_SD:
                exec('{} = thisTrials_Symbolic_SD[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Symbolic_SD" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        text_Symbolic_SD_pair1.setText(sym_stimuli_pair1)
        text_Symbolic_SD_pair2.setText(sym_stimuli_pair2)
        key_symbolic_SD.keys = []
        key_symbolic_SD.rt = []
        _key_symbolic_SD_allKeys = []
        # keep track of which components have finished
        Symbolic_SDComponents = [text_Symbolic_SD_pair1, text_Symbolic_SD_pair2, key_symbolic_SD]
        for thisComponent in Symbolic_SDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        
        # --- Run Routine "Symbolic_SD" ---
        while continueRoutine: #and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Symbolic_SD_pair1* updates
            if text_Symbolic_SD_pair1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Symbolic_SD_pair1.frameNStart = frameN  # exact frame index
                text_Symbolic_SD_pair1.tStart = t  # local t and not account for scr refresh
                text_Symbolic_SD_pair1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Symbolic_SD_pair1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Symbolic_SD_pair1.started')
                text_Symbolic_SD_pair1.setAutoDraw(True)
    
            # *sec1_key_resp* updates
            waitOnFlip = False
            if key_symbolic_SD.status == NOT_STARTED: #and tThisFlip >= resources.status == FINISHED-frameTolerance:
                # keep track of start time/frame for later
                key_symbolic_SD.frameNStart = frameN  # exact frame index
                key_symbolic_SD.tStart = t  # local t and not account for scr refresh
                key_symbolic_SD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Symbolic_SD_pair1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_symbolic_SD.started')
                key_symbolic_SD.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_symbolic_SD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_symbolic_SD.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_symbolic_SD.status == STARTED and not waitOnFlip:
                theseKeys = key_symbolic_SD.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_symbolic_SD_allKeys.extend(theseKeys)
                if len(_key_symbolic_SD_allKeys):
                    key_symbolic_SD.keys = _key_symbolic_SD_allKeys[-1].name  # just the last key pressed
                    key_symbolic_SD.rt = _key_symbolic_SD_allKeys[-1].rt
                    continueRoutine = False
                    # a response ends the routine
            
            # *text_Symbolic_SD_pair2* updates
            if text_Symbolic_SD_pair2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Symbolic_SD_pair2.frameNStart = frameN  # exact frame index
                text_Symbolic_SD_pair2.tStart = t  # local t and not account for scr refresh
                text_Symbolic_SD_pair2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Symbolic_SD_pair2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Symbolic_SD_pair2.started')
                text_Symbolic_SD_pair2.setAutoDraw(True)
            waitOnFlip = False
            if key_symbolic_SD.status == NOT_STARTED: #and tThisFlip >= resources.status == FINISHED-frameTolerance:
                # keep track of start time/frame for later
                key_symbolic_SD.frameNStart = frameN  # exact frame index
                key_symbolic_SD.tStart = t  # local t and not account for scr refresh
                key_symbolic_SD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_symbolic_SD, 'tStartRefresh')  # time at next scr refresh
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_symbolic_SD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_symbolic_SD.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_symbolic_SD.status == STARTED and not waitOnFlip:
                theseKeys = key_symbolic_SD.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_symbolic_SD_allKeys.extend(theseKeys)
                if len(_key_symbolic_SD_allKeys):
                    key_symbolic_SD.keys = _key_symbolic_SD_allKeys[-1].name  # just the last key pressed
                    key_symbolic_SD.rt = _key_symbolic_SD_allKeys[-1].rt
                    continueRoutine = False
                    # a response ends the routine
            
            # *key_symbolic_SD* updates
            waitOnFlip = False
            if key_symbolic_SD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_symbolic_SD.frameNStart = frameN  # exact frame index
                key_symbolic_SD.tStart = t  # local t and not account for scr refresh
                key_symbolic_SD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_symbolic_SD, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_symbolic_SD.started')
                key_symbolic_SD.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_symbolic_SD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_symbolic_SD.clearEvents, eventType='keyboard')  # clear events on next screen flip

            if key_symbolic_SD.status == STARTED and not waitOnFlip:
                theseKeys = key_symbolic_SD.getKeys(keyList=['left','right'], waitRelease=False)
                _key_symbolic_SD_allKeys.extend(theseKeys)
                if len(_key_symbolic_SD_allKeys):
                    key_symbolic_SD.keys = _key_symbolic_SD_allKeys[0].name  # just the first key pressed
                    key_symbolic_SD.rt = _key_symbolic_SD_allKeys[0].rt
                    # was this correct?
                    if (key_symbolic_SD.keys == str(correct_key)) or (key_symbolic_SD.keys == correct_key):
                        key_symbolic_SD.corr = 1
                    else:
                        key_symbolic_SD.corr = 0
                    
                    # a response ends the routine
                    row = ['symbolic', sym_stimuli_pair1, sym_stimuli_pair2, 
                    str(correct_key), key_symbolic_SD.keys, key_symbolic_SD.corr, 
                    t, tThisFlipGlobal, expInfo['participant'], 
                    psychopyVersion, expInfo['date'], expName,
                    expInfo['frameRate']]
                    with open(filename, 'a') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(row)                   
                    continueRoutine = False
                    
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Rouine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Symbolic_SDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Symbolic_SD" ---
        for thisComponent in Symbolic_SDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_symbolic_SD.keys in ['', [], None]:  # No response was made
            key_symbolic_SD.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               key_symbolic_SD.corr = 1;  # correct non-response
            else:
               key_symbolic_SD.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Symbolic_SD (TrialHandler)
        trials_Symbolic_SD.addData('key_symbolic_SD.keys',key_symbolic_SD.keys)
        print(key_symbolic_SD.keys)
        trials_Symbolic_SD.addData('key_symbolic_SD.corr', key_symbolic_SD.corr)
        print(key_symbolic_SD.corr)
        if key_symbolic_SD.keys != None:  # we had a response
            trials_Symbolic_SD.addData('key_symbolic_SD.rt', key_symbolic_SD.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
            
      # --- Prepare to start Routine "Section1 Instructions" ---
    continueRoutine = True
    routineForceEnded = False
      # update component parameters for each repeat
    sec1_key_resp.keys = []
    sec1_key_resp.rt = []
    _sec1_key_resp_allKeys = []
      # keep track of which components have finished       
    Sec1Components = [Sec1Screen, sec1_key_resp]
    for thisComponent in Sec1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
      # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
      # --- Run Routine "Sec1" ---
    while continueRoutine:
          # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
          # update/draw components on each frame
          
          # *Sec1Screen* updates
        if Sec1Screen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
              # keep track of start time/frame for later
            Sec1Screen.frameNStart = frameN  # exact frame index
            Sec1Screen.tStart = t  # local t and not account for scr refresh
            Sec1Screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sec1Screen, 'tStartRefresh')  # time at next scr refresh
              # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Sec1Screen.started')
            Sec1Screen.setAutoDraw(True)
          
          # *sec1_key_resp* updates
        waitOnFlip = False
        if sec1_key_resp.status == NOT_STARTED: #and tThisFlip >= resources.status == FINISHED-frameTolerance:
              # keep track of start time/frame for later
            sec1_key_resp.frameNStart = frameN  # exact frame index
            sec1_key_resp.tStart = t  # local t and not account for scr refresh
            sec1_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sec1_key_resp, 'tStartRefresh')  # time at next scr refresh
              # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sec1_key_resp.started')
            sec1_key_resp.status = STARTED
              # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sec1_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sec1_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sec1_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = sec1_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _sec1_key_resp_allKeys.extend(theseKeys)
            if len(_sec1_key_resp_allKeys):
                sec1_key_resp.keys = _sec1_key_resp_allKeys[-1].name  # just the last key pressed
                sec1_key_resp.rt = _sec1_key_resp_allKeys[-1].rt
                continueRoutine = False
                  # a response ends the routine
      
          
          # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
          
          # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Sec1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
          
          # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
      
      # --- Ending Routine "Sec1" ---
    for thisComponent in Sec1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
      #check responses
    if sec1_key_resp.keys in ['', [], None]:  # No response was made
        sec1_key_resp.keys = None
    thisExp.addData('sec1_key_resp.keys', sec1_key_resp.keys)
    if sec1_key_resp.keys != None:  # we had a response
        thisExp.addData('sec1_key_resp.rt', sec1_key_resp.rt)
    thisExp.nextEntry()
      #the Routine "sec1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()       
           
      # set up handler to look after randomisation of conditions etc
    trials_Nonsymbolic_SD = data.TrialHandler(nReps=nReps_nonsymbolic, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Nonsymbolic_pilot.csv'),
        seed=None, name='trials_Nonsymbolic_SD')
    thisExp.addLoop(trials_Nonsymbolic_SD)  # add the loop to the experiment
    thisTrials_Nonsymbolic_SD = trials_Nonsymbolic_SD.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Symbolic_SD.rgb)
    if thisTrials_Nonsymbolic_SD != None:
        for paramName in thisTrials_Nonsymbolic_SD:
            exec('{} = thisTrials_Nonsymbolic_SD[paramName]'.format(paramName))
    
    for thisTrials_Nonsymbolic_SD in trials_Nonsymbolic_SD:
        currentLoop = trials_Nonsymbolic_SD
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Symbolic_SD.rgb)
        if thisTrials_Nonsymbolic_SD != None:
            for paramName in thisTrials_Nonsymbolic_SD:
                exec('{} = thisTrials_Nonsymbolic_SD[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Symbolic_SD" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        image_Nonsymbolic_SD_pair1.setImage(stimuli_pair1)
        image_Nonsymbolic_SD_pair2.setImage(stimuli_pair2)
        key_nonsymbolic_SD.keys = []
        key_nonsymbolic_SD.rt = []
        _key_nonsymbolic_SD_allKeys = []
        # keep track of which components have finished
        Nonsymbolic_SDComponents = [image_Nonsymbolic_SD_pair1, image_Nonsymbolic_SD_pair2, key_nonsymbolic_SD]
        for thisComponent in Nonsymbolic_SDComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Symbolic_SD" ---
        while continueRoutine: #and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Symbolic_SD_pair1* updates
            if image_Nonsymbolic_SD_pair1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Nonsymbolic_SD_pair1.frameNStart = frameN  # exact frame index
                image_Nonsymbolic_SD_pair1.tStart = t  # local t and not account for scr refresh
                image_Nonsymbolic_SD_pair1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Nonsymbolic_SD_pair1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_Nonsymbolic_SD_pair1.started')
                image_Nonsymbolic_SD_pair1.setAutoDraw(True)
    
            # *sec1_key_resp* updates
            waitOnFlip = False
            if key_nonsymbolic_SD.status == NOT_STARTED: #and tThisFlip >= resources.status == FINISHED-frameTolerance:
                # keep track of start time/frame for later
                key_nonsymbolic_SD.frameNStart = frameN  # exact frame index
                key_nonsymbolic_SD.tStart = t  # local t and not account for scr refresh
                key_nonsymbolic_SD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_nonsymbolic_SD, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_nonsymbolic_SD.started')
                key_nonsymbolic_SD.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_nonsymbolic_SD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_nonsymbolic_SD.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_nonsymbolic_SD.status == STARTED and not waitOnFlip:
                theseKeys = key_nonsymbolic_SD.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_nonsymbolic_SD_allKeys.extend(theseKeys)
                if len(_key_nonsymbolic_SD_allKeys):
                    key_nonsymbolic_SD.keys = _key_nonsymbolic_SD_allKeys[-1].name  # just the last key pressed
                    key_nonsymbolic_SD.rt = _key_nonsymbolic_SD_allKeys[-1].rt
                    continueRoutine = False
            
            # *text_Symbolic_SD_pair2* updates
            if image_Nonsymbolic_SD_pair2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_Nonsymbolic_SD_pair2.frameNStart = frameN  # exact frame index
                image_Nonsymbolic_SD_pair2.tStart = t  # local t and not account for scr refresh
                image_Nonsymbolic_SD_pair2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_Nonsymbolic_SD_pair2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_Nonsymbolic_SD_pair2.started')
                image_Nonsymbolic_SD_pair2.setAutoDraw(True)
            waitOnFlip = False
            if key_nonsymbolic_SD.status == NOT_STARTED: #and tThisFlip >= resources.status == FINISHED-frameTolerance:
                # keep track of start time/frame for later
                key_nonsymbolic_SD.frameNStart = frameN  # exact frame index
                key_nonsymbolic_SD.tStart = t  # local t and not account for scr refresh
                key_nonsymbolic_SD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_nonsymbolic_SD, 'tStartRefresh')  # time at next scr refresh
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_nonsymbolic_SD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_nonsymbolic_SD.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_nonsymbolic_SD.status == STARTED and not waitOnFlip:
                theseKeys = key_nonsymbolic_SD.getKeys(keyList=['left', 'right'], waitRelease=False)
                _key_nonsymbolic_SD_allKeys.extend(theseKeys)
                if len(_key_nonsymbolic_SD_allKeys):
                    key_nonsymbolic_SD.keys = _key_nonsymbolic_SD_allKeys[-1].name  # just the last key pressed
                    key_nonsymbolic_SD.rt = _key_nonsymbolic_SD_allKeys[-1].rt
                    continueRoutine = False
                    # a response ends the routine
            # *key_symbolic_SD* updates
            waitOnFlip = False
            if key_nonsymbolic_SD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_nonsymbolic_SD.frameNStart = frameN  # exact frame index
                key_nonsymbolic_SD.tStart = t  # local t and not account for scr refresh
                key_nonsymbolic_SD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_nonsymbolic_SD, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_nonsymbolic_SD.started')
                key_nonsymbolic_SD.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_nonsymbolic_SD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_nonsymbolic_SD.clearEvents, eventType='keyboard')  # clear events on next screen flip

            if key_nonsymbolic_SD.status == STARTED and not waitOnFlip:
                theseKeys = key_nonsymbolic_SD.getKeys(keyList=['left','right'], waitRelease=False)
                _key_nonsymbolic_SD_allKeys.extend(theseKeys)
                if len(_key_nonsymbolic_SD_allKeys):
                    key_nonsymbolic_SD.keys = _key_nonsymbolic_SD_allKeys[0].name  # just the first key pressed
                    key_nonsymbolic_SD.rt = _key_nonsymbolic_SD_allKeys[0].rt
                    # was this correct?
                    if (key_nonsymbolic_SD.keys == str(correct_key)) or (key_nonsymbolic_SD.keys == correct_key):
                        key_nonsymbolic_SD.corr = 1
                    else:
                        key_nonsymbolic_SD.corr = 0
                    
                    # a response ends the routine
                    row = ['nonsymbolic', stimuli_pair1, stimuli_pair2, str(correct_key), 
                    key_nonsymbolic_SD.keys, key_nonsymbolic_SD.corr, t, tThisFlipGlobal, expInfo['participant'], 
                    psychopyVersion, expInfo['date'], expName, expInfo['frameRate']]
                    with open(filename, 'a') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(row)
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Nonsymbolic_SDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Symbolic_SD" ---
        for thisComponent in Nonsymbolic_SDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_nonsymbolic_SD.keys in ['', [], None]:  # No response was made
            key_nonsymbolic_SD.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               key_nonsymbolic_SD.corr = 1;  # correct non-response
            else:
               key_nonsymbolic_SD.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Symbolic_SD (TrialHandler)
        trials_Nonsymbolic_SD.addData('key_nonsymbolic_SD.keys',key_nonsymbolic_SD.keys)
        print(key_nonsymbolic_SD.keys)
        trials_Nonsymbolic_SD.addData('key_nonsymbolic_SD.corr', key_nonsymbolic_SD.corr)
        print(key_nonsymbolic_SD.corr)
        
        if key_nonsymbolic_SD.keys != None:  # we had a response
            trials_Nonsymbolic_SD.addData('key_nonsymbolic_SD.rt', key_nonsymbolic_SD.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)      
    break
        
        # --- Prepare to start Routine "ExitScreen" ---
continueRoutine = True
routineForceEnded = False
    # update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
    # keep track of which components have finished
ExitScreenComponents = [text, key_resp]
for thisComponent in ExitScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
    # reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1
    # --- Run Routine "ExitScreen" ---
while continueRoutine: # and routineTimer.getTime() < 10.0:
        # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
        
        # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
            # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.stopped')
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
            continueRoutine = False
        
        # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        
        # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExitScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
        
        # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ExitScreen" ---
for thisComponent in ExitScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()    

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
file_to_copy = './'+filename+'.csv'
destination_directory = './Proj2'
shutil.copy(file_to_copy, destination_directory)
core.quit()



 

