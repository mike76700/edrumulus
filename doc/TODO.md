# Edrumulus Road Map

The road map items are sorted by priority.

- [ ] **Increase data rate on UART serial bus for MIDI signals for prototype 5**

  The UART MIDI communication on prototype 5 is a direct connection to the Raspberry Pi and does
  not need a standard MIDI data rate. The faster the rate, the less samples are lost during MIDI
  signal transmission.

- [ ] **Improve rim shot detection**

  Especially for pads like the PDA-120L where the piezos are located near the edge, the rim shot detection does perform poorly.

- [ ] **Use rim switch theshold in dB**

  Do not use a linear parameter as it is implemented right now.

- [ ] **Introduce a first peak detection reliability**

  This can be used to improve the positional sensing. E.g., if the reliability is low, we could
  use the position of the last detected peak if it is close to the current peak in time (e.g., if
  we have a fast roll situation).

- [ ] **Improve Edrumulus/Drumgizmo usage on Raspberry Pi (Pi4, Pi 3+ and Pi Zero)**

  Maybe use ecasound to mix all the Drumgizmo audio channels in real-time to change the sound of the
  kit instantly without loading new samples in Drumgizmo.

- [ ] **Support positional sensing for rim shots**

- [ ] **Hot spot suppression on mesh pads with center piezo**

  Striking directly on the piezo results in detected velocity values which are much too high.

- [ ] **Fix EEPROM issue on the ESP32**

  The ESP32 storage seems to be unreliable (which is maybe caused by the way we are dealing with the threads), i.e.,
  some parameters are changed from time to time to a large value. Search for `### MARKER: ESP32 issue with read/write settings ###`
  in the code.

- [ ] **Improve dynamics for Drumgizmo**

  Could be done for official drum kits as well as self-recorded kit.

  To debug the dynamics:
  - Use MIDI file 1:10:127 as a reference.
  - Record audio.
  - Use DGEdit to estimate the powers.
  - Check the estimated powers.

  Maybe Bent can help out here.

- [ ] **Documentation (user manual)**

  Create an Edrumulus manual which describes the hardware/software setup, parameter description, HOWTOs, etc.

- [ ] **Should we consider pre-scan time high peaks for velocity estimation?**

- [ ] **For the ESP32 prototype, adjust the ADC_noise_peak_velocity_scaling in edrumulus.h correctly**

- [ ] **Algorihm documentation**

  The algorithm description should be improved. Especially, improve retrigger cancellation section.

