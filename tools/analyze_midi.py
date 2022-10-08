#!/usr/bin/env python3

#*******************************************************************************
# Copyright (c) 2022-2022
# Author(s): Volker Fischer
#*******************************************************************************
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
#*******************************************************************************

import time
import jack
import matplotlib.pyplot as plt


# initializations
client      = jack.Client('edrumulus_analyze_midi')
port_in     = client.midi_inports.register('input')
midi_values = [0] * 100
midi_pos    = [0] * 100


@client.set_process_callback
def process(frames):
  for offset, data in port_in.incoming_midi_events():
    if len(data) == 3:
      if int.from_bytes(data[0], "big") & 0xF0 == 0x90: # note on
        value = int.from_bytes(data[2], "big")
        midi_values.pop(0)
        midi_values.append(value)

      if int.from_bytes(data[0], "big") & 0xF0 == 0xB0: # controller
        key   = int.from_bytes(data[1], "big")
        value = int.from_bytes(data[2], "big")
        if key == 16: # positional sensing
          midi_pos.pop(0)
          midi_pos.append(value)


with client:
  print('close plot window to quit')
  port_in.connect('ttymidi:MIDI_in')
  fig, (ax0, ax1) = plt.subplots(2, 1)
  fignum          = fig.number
  plt.ion()

  while True:
    ax0.cla()
    ax0.set_title('MIDI Velocity')
    ax0.plot(midi_values)
    ax0.set_ylim(0, 127)
    ax0.grid(True)
    ax1.cla()
    ax1.set_title('MIDI Position')
    ax1.plot(midi_pos)
    ax1.set_ylim(0, 127)
    ax1.grid(True)
    plt.show()
    plt.pause(0.1)
    if not plt.fignum_exists(fignum): # if plot window is closed then quit
      break

