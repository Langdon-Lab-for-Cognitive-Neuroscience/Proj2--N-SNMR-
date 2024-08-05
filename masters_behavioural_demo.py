#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on March 26, 2024, at 01:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
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
    'PROLIFICID': '',
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

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Nidhi\\Psychopy\\masters_behavioural_demo\\masters_behavioural_demo.py',
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
    size=[1280, 720], fullscr=False, screen=0, 
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
    text='Welcome to the experiment! \n\nThere are two parts to this experiment, each section begins with an instruction screen followed by a block of training trials and then several experimental blocks. \n\nPlease press the SPACEBAR to proceed!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "MF_Instructions" ---
text_MF_instruct = visual.TextStim(win=win, name='text_MF_instruct',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_MF_instruct = keyboard.Keyboard()

# --- Initialize components for Routine "training_block_MF" ---

# --- Initialize components for Routine "MF_block" ---

# --- Initialize components for Routine "Attention_Check" ---

# --- Initialize components for Routine "Experiment_Instructions" ---
key_resp_exp_instruct = keyboard.Keyboard()
text_exp_instruct = visual.TextStim(win=win, name='text_exp_instruct',
    text='Training Block: \n\nFor this part of the experiment, arabic numerals or dot arrays will be briefly presented. Press the left arrow key to indicate that the dot array or arabic numeral was on the left side of the screen. Press the right arrow key to indicate that the dot array or arabic numeralwas on the right side of the screen. Please respond as quickly and accurately as possible. \n\nPlease press spacebar to begin!\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "NS_training_block" ---
image_training_pair1 = visual.ImageStim(
    win=win,
    name='image_training_pair1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_training_pair2 = visual.ImageStim(
    win=win,
    name='image_training_pair2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_training = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_blank500_test = visual.TextStim(win=win, name='text_blank500_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "S_Training_Block" ---

# --- Initialize components for Routine "blank500" ---
text_blank500_test = visual.TextStim(win=win, name='text_blank500_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Attention_Check" ---

# --- Initialize components for Routine "Instructions_Main_Exp" ---

# --- Initialize components for Routine "load_stimuli_lists" ---
# Run 'Begin Experiment' code from code_load_nonsymbolic_SD
#master list of stimuli files for nonsymbolic single digit condition
Nonsymbolic_SD_files_original = ['Nonsymbolic_SD_A.csv','Nonsymbolic_SD_B.csv','Nonsymbolic_SD_C.csv','Nonsymbolic_SD_D.csv']
#creates shuffled list of stimuli files
Nonsymbolic_SD_files = Nonsymbolic_SD_files_original
shuffle(Nonsymbolic_SD_files)

print(Nonsymbolic_SD_files)
# Run 'Begin Experiment' code from code_load_nonsymbolic_DD
#master list of nonsymbolic doubledigit stimuli files
Nonsymbolic_DD_files_original = ['Nonsymbolic_DD_A.csv','Nonsymbolic_DD_B.csv','Nonsymbolic_DD_C.csv','Nonsymbolic_DD_D.csv']
#creates shuffled list of stimuli file
Nonsymbolic_DD_files = Nonsymbolic_DD_files_original
shuffle(Nonsymbolic_DD_files)
print(Nonsymbolic_DD_files)

# --- Initialize components for Routine "select_stimuli_list_SD" ---
# Run 'Begin Experiment' code from code_select_stimuli_SD
Nonsymbolic_SD_curr = -1

# --- Initialize components for Routine "NonSymbolic_SD" ---
image_SD_pair1 = visual.ImageStim(
    win=win,
    name='image_SD_pair1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_SD_pair2 = visual.ImageStim(
    win=win,
    name='image_SD_pair2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(+0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_nonsymbolic_SD = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_blank500_test = visual.TextStim(win=win, name='text_blank500_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "select_stimuli_list_DD" ---
# Run 'Begin Experiment' code from code_select_stimuli_list_DD
Nonsymbolic_DD_curr = -1

# --- Initialize components for Routine "NonSymbolic_DD" ---
image_DD_pair1 = visual.ImageStim(
    win=win,
    name='image_DD_pair1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.5,0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_DD_pair2 = visual.ImageStim(
    win=win,
    name='image_DD_pair2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(+0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_nonsymbolic_DD = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_blank500_test = visual.TextStim(win=win, name='text_blank500_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

# --- Initialize components for Routine "blank500" ---
text_blank500_test = visual.TextStim(win=win, name='text_blank500_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Symbolic_DD" ---
text_Symbolic_DD_pair1 = visual.TextStim(win=win, name='text_Symbolic_DD_pair1',
    text='',
    font='Open Sans',
    pos=(-0.5, 0), height=0.25, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_Symbolic_DD_pair2 = visual.TextStim(win=win, name='text_Symbolic_DD_pair2',
    text='',
    font='Open Sans',
    pos=(0.5, 0), height=0.25, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_symbolic_DD = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_blank500_test = visual.TextStim(win=win, name='text_blank500_test',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EndofBlock" ---
text_EndofBlock = visual.TextStim(win=win, name='text_EndofBlock',
    text='+\nRest Block 10 Secs',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Attention_Check" ---

# --- Initialize components for Routine "ExitScreen" ---
text = visual.TextStim(win=win, name='text',
    text="Thanks for participating! Your prolific completion code is CDDSVOJS\n\nPress 'SPACEBAR' to exit the experiment",
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
    if WelcomeScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > WelcomeScreen.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            WelcomeScreen.tStop = t  # not accounting for scr refresh
            WelcomeScreen.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'WelcomeScreen.stopped')
            WelcomeScreen.setAutoDraw(False)
#downlaoding stimuli
    
    # *welcome_key_resp* updates
waitOnFlip = False
if welcome_key_resp.status == NOT_STARTED and tThisFlip >= resources.status == FINISHED-frameTolerance:
   # keep track of start time/frame for later
    welcome_key_resp.frameNStart = frameN  # exact frame index
    welcome_key_resp.tStart = t  # local t and not account for scr refresh
    welcome_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
    win.timeOnFlip(welcome_key_resp, 'tStartRefresh')  # time at next scr refresh
   # add timestamp to datafile
    thisExp.timestampOnFlip(win, 'welcome_key_resp.started')
    welcome_key_resp.status = STARTED
    #keyboard checking is just starting
    waitOnFlip = True
    win.callOnFlip(welcome_key_resp.clock.reset)  # t=0 on next screen flip
    win.callOnFlip(welcome_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
if welcome_key_resp.status == STARTED:
    # is it time to stop? (based on global clock, using actual start)
    if tThisFlipGlobal > welcome_key_resp.tStartRefresh + 20-frameTolerance:
        # keep track of stop time/frame for later
        welcome_key_resp.tStop = t  # not accounting for scr refresh
        welcome_key_resp.frameNStop = frameN  # exact frame index
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_key_resp.stopped')
        welcome_key_resp.status = FINISHED
if welcome_key_resp.status == STARTED and not waitOnFlip:
    theseKeys = welcome_key_resp.getKeys(keyList=['space'], waitRelease=False)
    _welcome_key_resp_allKeys.extend(theseKeys)
    if len(_welcome_key_resp_allKeys):
        welcome_key_resp.keys = _welcome_key_resp_allKeys[-1].name  # just the last key pressed
        welcome_key_resp.rt = _welcome_key_resp_allKeys[-1].rt
        # a response ends the routine
        continueRoutine = False

# check for quit (typically the Esc key)
if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
    core.quit()

# check if all components have finished
if not continueRoutine:  # a component has requested a forced-end of Routine
    routineForceEnded = True
   # break
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
# check responses
if welcome_key_resp.keys in ['', [], None]:  # No response was made
    welcome_key_resp.keys = None
thisExp.addData('welcome_key_resp.keys',welcome_key_resp.keys)
if welcome_key_resp.keys != None:  # we had a response
    thisExp.addData('welcome_key_resp.rt', welcome_key_resp.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "MF_Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_MF_instruct.keys = []
key_resp_MF_instruct.rt = []
_key_resp_MF_instruct_allKeys = []
# keep track of which components have finished
MF_InstructionsComponents = [text_MF_instruct, key_resp_MF_instruct]
for thisComponent in MF_InstructionsComponents:
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

# --- Run Routine "MF_Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_MF_instruct* updates
    if text_MF_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_MF_instruct.frameNStart = frameN  # exact frame index
        text_MF_instruct.tStart = t  # local t and not account for scr refresh
        text_MF_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_MF_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_MF_instruct.started')
        text_MF_instruct.setAutoDraw(True)
    if text_MF_instruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_MF_instruct.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_MF_instruct.tStop = t  # not accounting for scr refresh
            text_MF_instruct.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_MF_instruct.stopped')
            text_MF_instruct.setAutoDraw(False)
    
    # *key_resp_MF_instruct* updates
    waitOnFlip = False
    if key_resp_MF_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_MF_instruct.frameNStart = frameN  # exact frame index
        key_resp_MF_instruct.tStart = t  # local t and not account for scr refresh
        key_resp_MF_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_MF_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_MF_instruct.started')
        key_resp_MF_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_MF_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_MF_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_MF_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_MF_instruct.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_MF_instruct_allKeys.extend(theseKeys)
        if len(_key_resp_MF_instruct_allKeys):
            key_resp_MF_instruct.keys = _key_resp_MF_instruct_allKeys[-1].name  # just the last key pressed
            key_resp_MF_instruct.rt = _key_resp_MF_instruct_allKeys[-1].rt
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
    for thisComponent in MF_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "MF_Instructions" ---
for thisComponent in MF_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_MF_instruct.keys in ['', [], None]:  # No response was made
    key_resp_MF_instruct.keys = None
thisExp.addData('key_resp_MF_instruct.keys',key_resp_MF_instruct.keys)
if key_resp_MF_instruct.keys != None:  # we had a response
    thisExp.addData('key_resp_MF_instruct.rt', key_resp_MF_instruct.rt)
thisExp.nextEntry()
# the Routine "MF_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "training_block_MF" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    training_block_MFComponents = []
    for thisComponent in training_block_MFComponents:
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
    
    # --- Run Routine "training_block_MF" ---
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
        for thisComponent in training_block_MFComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_block_MF" ---
    for thisComponent in training_block_MFComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training_block_MF" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
MF_exp_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MF_stimuli_final.xlsx'),
    seed=1, name='MF_exp_trials')
thisExp.addLoop(MF_exp_trials)  # add the loop to the experiment
thisMF_exp_trial = MF_exp_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMF_exp_trial.rgb)
if thisMF_exp_trial != None:
    for paramName in thisMF_exp_trial:
        exec('{} = thisMF_exp_trial[paramName]'.format(paramName))

for thisMF_exp_trial in MF_exp_trials:
    currentLoop = MF_exp_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMF_exp_trial.rgb)
    if thisMF_exp_trial != None:
        for paramName in thisMF_exp_trial:
            exec('{} = thisMF_exp_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "MF_block" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    MF_blockComponents = []
    for thisComponent in MF_blockComponents:
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
    
    # --- Run Routine "MF_block" ---
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
        for thisComponent in MF_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "MF_block" ---
    for thisComponent in MF_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "MF_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'MF_exp_trials'


# --- Prepare to start Routine "Attention_Check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Attention_CheckComponents = []
for thisComponent in Attention_CheckComponents:
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

# --- Run Routine "Attention_Check" ---
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
    for thisComponent in Attention_CheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Attention_Check" ---
for thisComponent in Attention_CheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Attention_Check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Experiment_Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_exp_instruct.keys = []
key_resp_exp_instruct.rt = []
_key_resp_exp_instruct_allKeys = []
# keep track of which components have finished
Experiment_InstructionsComponents = [key_resp_exp_instruct, text_exp_instruct]
for thisComponent in Experiment_InstructionsComponents:
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

# --- Run Routine "Experiment_Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_exp_instruct* updates
    waitOnFlip = False
    if key_resp_exp_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_exp_instruct.frameNStart = frameN  # exact frame index
        key_resp_exp_instruct.tStart = t  # local t and not account for scr refresh
        key_resp_exp_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_exp_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_exp_instruct.started')
        key_resp_exp_instruct.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_exp_instruct.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_exp_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_exp_instruct.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_exp_instruct.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_exp_instruct_allKeys.extend(theseKeys)
        if len(_key_resp_exp_instruct_allKeys):
            key_resp_exp_instruct.keys = _key_resp_exp_instruct_allKeys[-1].name  # just the last key pressed
            key_resp_exp_instruct.rt = _key_resp_exp_instruct_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_exp_instruct* updates
    if text_exp_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_exp_instruct.frameNStart = frameN  # exact frame index
        text_exp_instruct.tStart = t  # local t and not account for scr refresh
        text_exp_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_exp_instruct, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_exp_instruct.started')
        text_exp_instruct.setAutoDraw(True)
    if text_exp_instruct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_exp_instruct.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            text_exp_instruct.tStop = t  # not accounting for scr refresh
            text_exp_instruct.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_exp_instruct.stopped')
            text_exp_instruct.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Experiment_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Experiment_Instructions" ---
for thisComponent in Experiment_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_exp_instruct.keys in ['', [], None]:  # No response was made
    key_resp_exp_instruct.keys = None
thisExp.addData('key_resp_exp_instruct.keys',key_resp_exp_instruct.keys)
if key_resp_exp_instruct.keys != None:  # we had a response
    thisExp.addData('key_resp_exp_instruct.rt', key_resp_exp_instruct.rt)
thisExp.nextEntry()
# the Routine "Experiment_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NS_trials_training = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ns_stimuli_training.xlsx'),
    seed=None, name='NS_trials_training')
thisExp.addLoop(NS_trials_training)  # add the loop to the experiment
thisNS_trials_training = NS_trials_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNS_trials_training.rgb)
if thisNS_trials_training != None:
    for paramName in thisNS_trials_training:
        exec('{} = thisNS_trials_training[paramName]'.format(paramName))

for thisNS_trials_training in NS_trials_training:
    currentLoop = NS_trials_training
    # abbreviate parameter names if possible (e.g. rgb = thisNS_trials_training.rgb)
    if thisNS_trials_training != None:
        for paramName in thisNS_trials_training:
            exec('{} = thisNS_trials_training[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS_training_block" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    image_training_pair1.setImage(training_pair1)
    image_training_pair2.setImage(training_pair2)
    key_resp_training.keys = []
    key_resp_training.rt = []
    _key_resp_training_allKeys = []
    # keep track of which components have finished
    NS_training_blockComponents = [image_training_pair1, image_training_pair2, key_resp_training]
    for thisComponent in NS_training_blockComponents:
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
    
    # --- Run Routine "NS_training_block" ---
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_training_pair1* updates
        if image_training_pair1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_training_pair1.frameNStart = frameN  # exact frame index
            image_training_pair1.tStart = t  # local t and not account for scr refresh
            image_training_pair1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_training_pair1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_training_pair1.started')
            image_training_pair1.setAutoDraw(True)
        if image_training_pair1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_training_pair1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_training_pair1.tStop = t  # not accounting for scr refresh
                image_training_pair1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_training_pair1.stopped')
                image_training_pair1.setAutoDraw(False)
        
        # *image_training_pair2* updates
        if image_training_pair2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_training_pair2.frameNStart = frameN  # exact frame index
            image_training_pair2.tStart = t  # local t and not account for scr refresh
            image_training_pair2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_training_pair2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_training_pair2.started')
            image_training_pair2.setAutoDraw(True)
        if image_training_pair2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_training_pair2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_training_pair2.tStop = t  # not accounting for scr refresh
                image_training_pair2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_training_pair2.stopped')
                image_training_pair2.setAutoDraw(False)
        
        # *key_resp_training* updates
        waitOnFlip = False
        if key_resp_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_training.frameNStart = frameN  # exact frame index
            key_resp_training.tStart = t  # local t and not account for scr refresh
            key_resp_training.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_training, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_training.started')
            key_resp_training.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_training.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_training.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_training.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_training.tStop = t  # not accounting for scr refresh
                key_resp_training.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_training.stopped')
                key_resp_training.status = FINISHED
        if key_resp_training.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_training.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_training_allKeys.extend(theseKeys)
            if len(_key_resp_training_allKeys):
                key_resp_training.keys = _key_resp_training_allKeys[-1].name  # just the last key pressed
                key_resp_training.rt = _key_resp_training_allKeys[-1].rt
                # was this correct?
                if (key_resp_training.keys == str(correct_key)) or (key_resp_training.keys == correct_key):
                    key_resp_training.corr = 1
                else:
                    key_resp_training.corr = 0
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
        for thisComponent in NS_training_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS_training_block" ---
    for thisComponent in NS_training_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_training.keys in ['', [], None]:  # No response was made
        key_resp_training.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           key_resp_training.corr = 1;  # correct non-response
        else:
           key_resp_training.corr = 0;  # failed to respond (incorrectly)
    # store data for NS_trials_training (TrialHandler)
    NS_trials_training.addData('key_resp_training.keys',key_resp_training.keys)
    NS_trials_training.addData('key_resp_training.corr', key_resp_training.corr)
    if key_resp_training.keys != None:  # we had a response
        NS_trials_training.addData('key_resp_training.rt', key_resp_training.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [text_blank500_test]
    for thisComponent in blank500Components:
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
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank500_test* updates
        if text_blank500_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blank500_test.frameNStart = frameN  # exact frame index
            text_blank500_test.tStart = t  # local t and not account for scr refresh
            text_blank500_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blank500_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blank500_test.started')
            text_blank500_test.setAutoDraw(True)
        if text_blank500_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blank500_test.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_blank500_test.tStop = t  # not accounting for scr refresh
                text_blank500_test.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blank500_test.stopped')
                text_blank500_test.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NS_trials_training'


# set up handler to look after randomisation of conditions etc
S_trials_training = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='S_trials_training')
thisExp.addLoop(S_trials_training)  # add the loop to the experiment
thisS_trials_training = S_trials_training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisS_trials_training.rgb)
if thisS_trials_training != None:
    for paramName in thisS_trials_training:
        exec('{} = thisS_trials_training[paramName]'.format(paramName))

for thisS_trials_training in S_trials_training:
    currentLoop = S_trials_training
    # abbreviate parameter names if possible (e.g. rgb = thisS_trials_training.rgb)
    if thisS_trials_training != None:
        for paramName in thisS_trials_training:
            exec('{} = thisS_trials_training[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "S_Training_Block" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    S_Training_BlockComponents = []
    for thisComponent in S_Training_BlockComponents:
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
    
    # --- Run Routine "S_Training_Block" ---
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
        for thisComponent in S_Training_BlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "S_Training_Block" ---
    for thisComponent in S_Training_BlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "S_Training_Block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [text_blank500_test]
    for thisComponent in blank500Components:
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
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_blank500_test* updates
        if text_blank500_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_blank500_test.frameNStart = frameN  # exact frame index
            text_blank500_test.tStart = t  # local t and not account for scr refresh
            text_blank500_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_blank500_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_blank500_test.started')
            text_blank500_test.setAutoDraw(True)
        if text_blank500_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_blank500_test.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_blank500_test.tStop = t  # not accounting for scr refresh
                text_blank500_test.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blank500_test.stopped')
                text_blank500_test.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'S_trials_training'


# --- Prepare to start Routine "Attention_Check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Attention_CheckComponents = []
for thisComponent in Attention_CheckComponents:
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

# --- Run Routine "Attention_Check" ---
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
    for thisComponent in Attention_CheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Attention_Check" ---
for thisComponent in Attention_CheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Attention_Check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions_Main_Exp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Instructions_Main_ExpComponents = []
for thisComponent in Instructions_Main_ExpComponents:
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

# --- Run Routine "Instructions_Main_Exp" ---
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
    for thisComponent in Instructions_Main_ExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_Main_Exp" ---
for thisComponent in Instructions_Main_ExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions_Main_Exp" was not non-slip safe, so reset the non-slip timer
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
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_randomizer.rgb)
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
    SD_stimuli_list_randomizer = data.TrialHandler(nReps=nReps_nonsymbolic_SD, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SD_stimuli_list_randomizer')
    thisExp.addLoop(SD_stimuli_list_randomizer)  # add the loop to the experiment
    thisSD_stimulus_list_randomizer = SD_stimuli_list_randomizer.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSD_stimulus_list_randomizer.rgb)
    if thisSD_stimulus_list_randomizer != None:
        for paramName in thisSD_stimulus_list_randomizer:
            exec('{} = thisSD_stimulus_list_randomizer[paramName]'.format(paramName))
    
    for thisSD_stimulus_list_randomizer in SD_stimuli_list_randomizer:
        currentLoop = SD_stimuli_list_randomizer
        # abbreviate parameter names if possible (e.g. rgb = thisSD_stimulus_list_randomizer.rgb)
        if thisSD_stimulus_list_randomizer != None:
            for paramName in thisSD_stimulus_list_randomizer:
                exec('{} = thisSD_stimulus_list_randomizer[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "select_stimuli_list_SD" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_select_stimuli_SD
        print(Nonsymbolic_SD_files[Nonsymbolic_SD_curr+1])
        print(Nonsymbolic_SD_curr+1)
        # keep track of which components have finished
        select_stimuli_list_SDComponents = []
        for thisComponent in select_stimuli_list_SDComponents:
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
        
        # --- Run Routine "select_stimuli_list_SD" ---
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
            for thisComponent in select_stimuli_list_SDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "select_stimuli_list_SD" ---
        for thisComponent in select_stimuli_list_SDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_select_stimuli_SD
        Nonsymbolic_SD_curr += 1
        # the Routine "select_stimuli_list_SD" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_nonsymbolic_SD = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(Nonsymbolic_SD_files[Nonsymbolic_SD_curr]),
            seed=None, name='trials_nonsymbolic_SD')
        thisExp.addLoop(trials_nonsymbolic_SD)  # add the loop to the experiment
        thisTrials_nonsymbolic_SD = trials_nonsymbolic_SD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_nonsymbolic_SD.rgb)
        if thisTrials_nonsymbolic_SD != None:
            for paramName in thisTrials_nonsymbolic_SD:
                exec('{} = thisTrials_nonsymbolic_SD[paramName]'.format(paramName))
        
        for thisTrials_nonsymbolic_SD in trials_nonsymbolic_SD:
            currentLoop = trials_nonsymbolic_SD
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_nonsymbolic_SD.rgb)
            if thisTrials_nonsymbolic_SD != None:
                for paramName in thisTrials_nonsymbolic_SD:
                    exec('{} = thisTrials_nonsymbolic_SD[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "NonSymbolic_SD" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_SD_pair1.setImage(training_left)
            image_SD_pair2.setImage(training_right)
            key_nonsymbolic_SD.keys = []
            key_nonsymbolic_SD.rt = []
            _key_nonsymbolic_SD_allKeys = []
            # keep track of which components have finished
            NonSymbolic_SDComponents = [image_SD_pair1, image_SD_pair2, key_nonsymbolic_SD]
            for thisComponent in NonSymbolic_SDComponents:
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
            
            # --- Run Routine "NonSymbolic_SD" ---
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_SD_pair1* updates
                if image_SD_pair1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_SD_pair1.frameNStart = frameN  # exact frame index
                    image_SD_pair1.tStart = t  # local t and not account for scr refresh
                    image_SD_pair1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_SD_pair1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_SD_pair1.started')
                    image_SD_pair1.setAutoDraw(True)
                if image_SD_pair1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_SD_pair1.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_SD_pair1.tStop = t  # not accounting for scr refresh
                        image_SD_pair1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_SD_pair1.stopped')
                        image_SD_pair1.setAutoDraw(False)
                
                # *image_SD_pair2* updates
                if image_SD_pair2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_SD_pair2.frameNStart = frameN  # exact frame index
                    image_SD_pair2.tStart = t  # local t and not account for scr refresh
                    image_SD_pair2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_SD_pair2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_SD_pair2.started')
                    image_SD_pair2.setAutoDraw(True)
                if image_SD_pair2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_SD_pair2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_SD_pair2.tStop = t  # not accounting for scr refresh
                        image_SD_pair2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_SD_pair2.stopped')
                        image_SD_pair2.setAutoDraw(False)
                
                # *key_nonsymbolic_SD* updates
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
                if key_nonsymbolic_SD.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_nonsymbolic_SD.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        key_nonsymbolic_SD.tStop = t  # not accounting for scr refresh
                        key_nonsymbolic_SD.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_nonsymbolic_SD.stopped')
                        key_nonsymbolic_SD.status = FINISHED
                if key_nonsymbolic_SD.status == STARTED and not waitOnFlip:
                    theseKeys = key_nonsymbolic_SD.getKeys(keyList=['left','right'], waitRelease=False)
                    _key_nonsymbolic_SD_allKeys.extend(theseKeys)
                    if len(_key_nonsymbolic_SD_allKeys):
                        key_nonsymbolic_SD.keys = _key_nonsymbolic_SD_allKeys[-1].name  # just the last key pressed
                        key_nonsymbolic_SD.rt = _key_nonsymbolic_SD_allKeys[-1].rt
                        # was this correct?
                        if (key_nonsymbolic_SD.keys == str(correct_key)) or (key_nonsymbolic_SD.keys == correct_key):
                            key_nonsymbolic_SD.corr = 1
                        else:
                            key_nonsymbolic_SD.corr = 0
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
                for thisComponent in NonSymbolic_SDComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "NonSymbolic_SD" ---
            for thisComponent in NonSymbolic_SDComponents:
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
            # store data for trials_nonsymbolic_SD (TrialHandler)
            trials_nonsymbolic_SD.addData('key_nonsymbolic_SD.keys',key_nonsymbolic_SD.keys)
            trials_nonsymbolic_SD.addData('key_nonsymbolic_SD.corr', key_nonsymbolic_SD.corr)
            if key_nonsymbolic_SD.keys != None:  # we had a response
                trials_nonsymbolic_SD.addData('key_nonsymbolic_SD.rt', key_nonsymbolic_SD.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # --- Prepare to start Routine "blank500" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            blank500Components = [text_blank500_test]
            for thisComponent in blank500Components:
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
            
            # --- Run Routine "blank500" ---
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_blank500_test* updates
                if text_blank500_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_blank500_test.frameNStart = frameN  # exact frame index
                    text_blank500_test.tStart = t  # local t and not account for scr refresh
                    text_blank500_test.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_blank500_test, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_blank500_test.started')
                    text_blank500_test.setAutoDraw(True)
                if text_blank500_test.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_blank500_test.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_blank500_test.tStop = t  # not accounting for scr refresh
                        text_blank500_test.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_blank500_test.stopped')
                        text_blank500_test.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blank500" ---
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_nonsymbolic_SD'
        
    # completed nReps_nonsymbolic_SD repeats of 'SD_stimuli_list_randomizer'
    
    
    # set up handler to look after randomisation of conditions etc
    DD_stimuli_list_randomizer = data.TrialHandler(nReps=nReps_nonsymbolic_DD, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='DD_stimuli_list_randomizer')
    thisExp.addLoop(DD_stimuli_list_randomizer)  # add the loop to the experiment
    thisDD_stimulus_list_randomizer = DD_stimuli_list_randomizer.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDD_stimulus_list_randomizer.rgb)
    if thisDD_stimulus_list_randomizer != None:
        for paramName in thisDD_stimulus_list_randomizer:
            exec('{} = thisDD_stimulus_list_randomizer[paramName]'.format(paramName))
    
    for thisDD_stimulus_list_randomizer in DD_stimuli_list_randomizer:
        currentLoop = DD_stimuli_list_randomizer
        # abbreviate parameter names if possible (e.g. rgb = thisDD_stimulus_list_randomizer.rgb)
        if thisDD_stimulus_list_randomizer != None:
            for paramName in thisDD_stimulus_list_randomizer:
                exec('{} = thisDD_stimulus_list_randomizer[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "select_stimuli_list_DD" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_select_stimuli_list_DD
        print(Nonsymbolic_DD_files[Nonsymbolic_DD_curr+1])
        print(Nonsymbolic_DD_curr+1)
        # keep track of which components have finished
        select_stimuli_list_DDComponents = []
        for thisComponent in select_stimuli_list_DDComponents:
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
        
        # --- Run Routine "select_stimuli_list_DD" ---
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
            for thisComponent in select_stimuli_list_DDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "select_stimuli_list_DD" ---
        for thisComponent in select_stimuli_list_DDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code_select_stimuli_list_DD
        Nonsymbolic_DD_curr += 1
        # the Routine "select_stimuli_list_DD" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_nonsymbolic_DD = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(Nonsymbolic_DD_files[Nonsymbolic_DD_curr]),
            seed=None, name='trials_nonsymbolic_DD')
        thisExp.addLoop(trials_nonsymbolic_DD)  # add the loop to the experiment
        thisTrials_nonsymbolic_DD = trials_nonsymbolic_DD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_nonsymbolic_DD.rgb)
        if thisTrials_nonsymbolic_DD != None:
            for paramName in thisTrials_nonsymbolic_DD:
                exec('{} = thisTrials_nonsymbolic_DD[paramName]'.format(paramName))
        
        for thisTrials_nonsymbolic_DD in trials_nonsymbolic_DD:
            currentLoop = trials_nonsymbolic_DD
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_nonsymbolic_DD.rgb)
            if thisTrials_nonsymbolic_DD != None:
                for paramName in thisTrials_nonsymbolic_DD:
                    exec('{} = thisTrials_nonsymbolic_DD[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "NonSymbolic_DD" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            image_DD_pair1.setImage(stimuli_pair1)
            image_DD_pair2.setImage(stimuli_pair2)
            key_nonsymbolic_DD.keys = []
            key_nonsymbolic_DD.rt = []
            _key_nonsymbolic_DD_allKeys = []
            # keep track of which components have finished
            NonSymbolic_DDComponents = [image_DD_pair1, image_DD_pair2, key_nonsymbolic_DD]
            for thisComponent in NonSymbolic_DDComponents:
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
            
            # --- Run Routine "NonSymbolic_DD" ---
            while continueRoutine and routineTimer.getTime() < 10.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_DD_pair1* updates
                if image_DD_pair1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_DD_pair1.frameNStart = frameN  # exact frame index
                    image_DD_pair1.tStart = t  # local t and not account for scr refresh
                    image_DD_pair1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_DD_pair1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_DD_pair1.started')
                    image_DD_pair1.setAutoDraw(True)
                if image_DD_pair1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_DD_pair1.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_DD_pair1.tStop = t  # not accounting for scr refresh
                        image_DD_pair1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_DD_pair1.stopped')
                        image_DD_pair1.setAutoDraw(False)
                
                # *image_DD_pair2* updates
                if image_DD_pair2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_DD_pair2.frameNStart = frameN  # exact frame index
                    image_DD_pair2.tStart = t  # local t and not account for scr refresh
                    image_DD_pair2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_DD_pair2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_DD_pair2.started')
                    image_DD_pair2.setAutoDraw(True)
                if image_DD_pair2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_DD_pair2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_DD_pair2.tStop = t  # not accounting for scr refresh
                        image_DD_pair2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_DD_pair2.stopped')
                        image_DD_pair2.setAutoDraw(False)
                
                # *key_nonsymbolic_DD* updates
                waitOnFlip = False
                if key_nonsymbolic_DD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_nonsymbolic_DD.frameNStart = frameN  # exact frame index
                    key_nonsymbolic_DD.tStart = t  # local t and not account for scr refresh
                    key_nonsymbolic_DD.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_nonsymbolic_DD, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_nonsymbolic_DD.started')
                    key_nonsymbolic_DD.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_nonsymbolic_DD.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_nonsymbolic_DD.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_nonsymbolic_DD.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_nonsymbolic_DD.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        key_nonsymbolic_DD.tStop = t  # not accounting for scr refresh
                        key_nonsymbolic_DD.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_nonsymbolic_DD.stopped')
                        key_nonsymbolic_DD.status = FINISHED
                if key_nonsymbolic_DD.status == STARTED and not waitOnFlip:
                    theseKeys = key_nonsymbolic_DD.getKeys(keyList=['left','right'], waitRelease=False)
                    _key_nonsymbolic_DD_allKeys.extend(theseKeys)
                    if len(_key_nonsymbolic_DD_allKeys):
                        key_nonsymbolic_DD.keys = _key_nonsymbolic_DD_allKeys[0].name  # just the first key pressed
                        key_nonsymbolic_DD.rt = _key_nonsymbolic_DD_allKeys[0].rt
                        # was this correct?
                        if (key_nonsymbolic_DD.keys == str(correct_key)) or (key_nonsymbolic_DD.keys == correct_key):
                            key_nonsymbolic_DD.corr = 1
                        else:
                            key_nonsymbolic_DD.corr = 0
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
                for thisComponent in NonSymbolic_DDComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "NonSymbolic_DD" ---
            for thisComponent in NonSymbolic_DDComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_nonsymbolic_DD.keys in ['', [], None]:  # No response was made
                key_nonsymbolic_DD.keys = None
                # was no response the correct answer?!
                if str(correct_key).lower() == 'none':
                   key_nonsymbolic_DD.corr = 1;  # correct non-response
                else:
                   key_nonsymbolic_DD.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_nonsymbolic_DD (TrialHandler)
            trials_nonsymbolic_DD.addData('key_nonsymbolic_DD.keys',key_nonsymbolic_DD.keys)
            trials_nonsymbolic_DD.addData('key_nonsymbolic_DD.corr', key_nonsymbolic_DD.corr)
            if key_nonsymbolic_DD.keys != None:  # we had a response
                trials_nonsymbolic_DD.addData('key_nonsymbolic_DD.rt', key_nonsymbolic_DD.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-10.000000)
            
            # --- Prepare to start Routine "blank500" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            blank500Components = [text_blank500_test]
            for thisComponent in blank500Components:
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
            
            # --- Run Routine "blank500" ---
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_blank500_test* updates
                if text_blank500_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_blank500_test.frameNStart = frameN  # exact frame index
                    text_blank500_test.tStart = t  # local t and not account for scr refresh
                    text_blank500_test.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_blank500_test, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_blank500_test.started')
                    text_blank500_test.setAutoDraw(True)
                if text_blank500_test.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_blank500_test.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_blank500_test.tStop = t  # not accounting for scr refresh
                        text_blank500_test.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_blank500_test.stopped')
                        text_blank500_test.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank500Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blank500" ---
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_nonsymbolic_DD'
        
    # completed nReps_nonsymbolic_DD repeats of 'DD_stimuli_list_randomizer'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_Symbolic_SD = data.TrialHandler(nReps=nReps_symbolic_SD, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Symbolic_SD.csv'),
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
        while continueRoutine and routineTimer.getTime() < 10.0:
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
            if text_Symbolic_SD_pair1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Symbolic_SD_pair1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Symbolic_SD_pair1.tStop = t  # not accounting for scr refresh
                    text_Symbolic_SD_pair1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_Symbolic_SD_pair1.stopped')
                    text_Symbolic_SD_pair1.setAutoDraw(False)
            
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
            if text_Symbolic_SD_pair2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Symbolic_SD_pair2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Symbolic_SD_pair2.tStop = t  # not accounting for scr refresh
                    text_Symbolic_SD_pair2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_Symbolic_SD_pair2.stopped')
                    text_Symbolic_SD_pair2.setAutoDraw(False)
            
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
            if key_symbolic_SD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_symbolic_SD.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    key_symbolic_SD.tStop = t  # not accounting for scr refresh
                    key_symbolic_SD.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_symbolic_SD.stopped')
                    key_symbolic_SD.status = FINISHED
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
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
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
        trials_Symbolic_SD.addData('key_symbolic_SD.corr', key_symbolic_SD.corr)
        if key_symbolic_SD.keys != None:  # we had a response
            trials_Symbolic_SD.addData('key_symbolic_SD.rt', key_symbolic_SD.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        blank500Components = [text_blank500_test]
        for thisComponent in blank500Components:
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
        
        # --- Run Routine "blank500" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blank500_test* updates
            if text_blank500_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blank500_test.frameNStart = frameN  # exact frame index
                text_blank500_test.tStart = t  # local t and not account for scr refresh
                text_blank500_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blank500_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blank500_test.started')
                text_blank500_test.setAutoDraw(True)
            if text_blank500_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_blank500_test.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_blank500_test.tStop = t  # not accounting for scr refresh
                    text_blank500_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_blank500_test.stopped')
                    text_blank500_test.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed nReps_symbolic_SD repeats of 'trials_Symbolic_SD'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_Symbolic_DD = data.TrialHandler(nReps=nReps_symbolic_DD, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Symbolic_DD.csv'),
        seed=None, name='trials_Symbolic_DD')
    thisExp.addLoop(trials_Symbolic_DD)  # add the loop to the experiment
    thisTrials_Symbolic_DD = trials_Symbolic_DD.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Symbolic_DD.rgb)
    if thisTrials_Symbolic_DD != None:
        for paramName in thisTrials_Symbolic_DD:
            exec('{} = thisTrials_Symbolic_DD[paramName]'.format(paramName))
    
    for thisTrials_Symbolic_DD in trials_Symbolic_DD:
        currentLoop = trials_Symbolic_DD
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Symbolic_DD.rgb)
        if thisTrials_Symbolic_DD != None:
            for paramName in thisTrials_Symbolic_DD:
                exec('{} = thisTrials_Symbolic_DD[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Symbolic_DD" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        text_Symbolic_DD_pair1.setText(sym_stimuli_pair1)
        text_Symbolic_DD_pair2.setText(sym_stimuli_pair2)
        key_symbolic_DD.keys = []
        key_symbolic_DD.rt = []
        _key_symbolic_DD_allKeys = []
        # keep track of which components have finished
        Symbolic_DDComponents = [text_Symbolic_DD_pair1, text_Symbolic_DD_pair2, key_symbolic_DD]
        for thisComponent in Symbolic_DDComponents:
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
        
        # --- Run Routine "Symbolic_DD" ---
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Symbolic_DD_pair1* updates
            if text_Symbolic_DD_pair1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Symbolic_DD_pair1.frameNStart = frameN  # exact frame index
                text_Symbolic_DD_pair1.tStart = t  # local t and not account for scr refresh
                text_Symbolic_DD_pair1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Symbolic_DD_pair1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Symbolic_DD_pair1.started')
                text_Symbolic_DD_pair1.setAutoDraw(True)
            if text_Symbolic_DD_pair1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Symbolic_DD_pair1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Symbolic_DD_pair1.tStop = t  # not accounting for scr refresh
                    text_Symbolic_DD_pair1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_Symbolic_DD_pair1.stopped')
                    text_Symbolic_DD_pair1.setAutoDraw(False)
            
            # *text_Symbolic_DD_pair2* updates
            if text_Symbolic_DD_pair2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Symbolic_DD_pair2.frameNStart = frameN  # exact frame index
                text_Symbolic_DD_pair2.tStart = t  # local t and not account for scr refresh
                text_Symbolic_DD_pair2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Symbolic_DD_pair2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Symbolic_DD_pair2.started')
                text_Symbolic_DD_pair2.setAutoDraw(True)
            if text_Symbolic_DD_pair2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Symbolic_DD_pair2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Symbolic_DD_pair2.tStop = t  # not accounting for scr refresh
                    text_Symbolic_DD_pair2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_Symbolic_DD_pair2.stopped')
                    text_Symbolic_DD_pair2.setAutoDraw(False)
            
            # *key_symbolic_DD* updates
            waitOnFlip = False
            if key_symbolic_DD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_symbolic_DD.frameNStart = frameN  # exact frame index
                key_symbolic_DD.tStart = t  # local t and not account for scr refresh
                key_symbolic_DD.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_symbolic_DD, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_symbolic_DD.started')
                key_symbolic_DD.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_symbolic_DD.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_symbolic_DD.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_symbolic_DD.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_symbolic_DD.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    key_symbolic_DD.tStop = t  # not accounting for scr refresh
                    key_symbolic_DD.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_symbolic_DD.stopped')
                    key_symbolic_DD.status = FINISHED
            if key_symbolic_DD.status == STARTED and not waitOnFlip:
                theseKeys = key_symbolic_DD.getKeys(keyList=['left','right'], waitRelease=False)
                _key_symbolic_DD_allKeys.extend(theseKeys)
                if len(_key_symbolic_DD_allKeys):
                    key_symbolic_DD.keys = _key_symbolic_DD_allKeys[0].name  # just the first key pressed
                    key_symbolic_DD.rt = _key_symbolic_DD_allKeys[0].rt
                    # was this correct?
                    if (key_symbolic_DD.keys == str(correct_key)) or (key_symbolic_DD.keys == correct_key):
                        key_symbolic_DD.corr = 1
                    else:
                        key_symbolic_DD.corr = 0
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
            for thisComponent in Symbolic_DDComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Symbolic_DD" ---
        for thisComponent in Symbolic_DDComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_symbolic_DD.keys in ['', [], None]:  # No response was made
            key_symbolic_DD.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               key_symbolic_DD.corr = 1;  # correct non-response
            else:
               key_symbolic_DD.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Symbolic_DD (TrialHandler)
        trials_Symbolic_DD.addData('key_symbolic_DD.keys',key_symbolic_DD.keys)
        trials_Symbolic_DD.addData('key_symbolic_DD.corr', key_symbolic_DD.corr)
        if key_symbolic_DD.keys != None:  # we had a response
            trials_Symbolic_DD.addData('key_symbolic_DD.rt', key_symbolic_DD.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        blank500Components = [text_blank500_test]
        for thisComponent in blank500Components:
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
        
        # --- Run Routine "blank500" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_blank500_test* updates
            if text_blank500_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_blank500_test.frameNStart = frameN  # exact frame index
                text_blank500_test.tStart = t  # local t and not account for scr refresh
                text_blank500_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_blank500_test, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_blank500_test.started')
                text_blank500_test.setAutoDraw(True)
            if text_blank500_test.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_blank500_test.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_blank500_test.tStop = t  # not accounting for scr refresh
                    text_blank500_test.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_blank500_test.stopped')
                    text_blank500_test.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed nReps_symbolic_DD repeats of 'trials_Symbolic_DD'
    
    
    # --- Prepare to start Routine "EndofBlock" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    EndofBlockComponents = [text_EndofBlock]
    for thisComponent in EndofBlockComponents:
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
    
    # --- Run Routine "EndofBlock" ---
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_EndofBlock* updates
        if text_EndofBlock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_EndofBlock.frameNStart = frameN  # exact frame index
            text_EndofBlock.tStart = t  # local t and not account for scr refresh
            text_EndofBlock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_EndofBlock, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_EndofBlock.started')
            text_EndofBlock.setAutoDraw(True)
        if text_EndofBlock.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_EndofBlock.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_EndofBlock.tStop = t  # not accounting for scr refresh
                text_EndofBlock.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_EndofBlock.stopped')
                text_EndofBlock.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndofBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndofBlock" ---
    for thisComponent in EndofBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
# completed 1.0 repeats of 'block_randomizer'


# --- Prepare to start Routine "Attention_Check" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Attention_CheckComponents = []
for thisComponent in Attention_CheckComponents:
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

# --- Run Routine "Attention_Check" ---
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
    for thisComponent in Attention_CheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Attention_Check" ---
for thisComponent in Attention_CheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Attention_Check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
while continueRoutine and routineTimer.getTime() < 10.0:
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
        theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
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
core.quit()
