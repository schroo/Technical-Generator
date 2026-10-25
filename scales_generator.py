import streamlit as st
import random

st.header("Technical Test Random Generator", divider="rainbow")

Scales = [
    "C Major Scale",
    "C Minor Harmonic",
    "C Minor Melodic",
    "C Chromatic",
    
    "C# Major Scale",
    "C# Minor Harmonic",
    "C# Minor Melodic",
    "C# Chromatic",
    
    "D Major Scale",
    "D Minor Harmonic",
    "D Minor Melodic",
    "D Chromatic",
    
    "Eb Major Scale",
    "Eb Minor Harmonic",
    "Eb Minor Melodic",
    "Eb Chromatic",
    
    "E Major Scale",
    "E Minor Harmonic",
    "E Minor Melodic",
    "E Chromatic",
    
    "F Major Scale",
    "F Minor Harmonic",
    "F Minor Melodic",
    "F Chromatic",
    
    "F# Major Scale",
    "F# Minor Harmonic",
    "F# Minor Melodic",
    "F# Chromatic",
    
    "G Major Scale",
    "G Minor Harmonic",
    "G Minor Melodic",
    "G Chromatic",
    
    "Ab Major Scale",
    "Ab Minor Harmonic",
    "Ab Minor Melodic",
    "Ab Chromatic",
    
    "A Major Scale",
    "A Minor Harmonic",
    "A Minor Melodic",
    "A Chromatic",

    "Bb Major Scale",
    "Bb Minor Harmonic",
    "Bb Minor Melodic",
    "Bb Chromatic",
    
    "B Major Scale",
    "B Minor Harmonic",
    "B Minor Melodic",
    "B Chromatic"
]

Appregios = [
    "C Major Arpeggio",
    "C Minor Arpeggio",
    "C Dominant 7th",
    "C Diminished 7th",

    "C# Major Arpeggio",
    "C# Minor Arpeggio",
    "C# Dominant 7th",
    "C# Diminished 7th",

    "D Major Arpeggio",
    "D Minor Arpeggio",
    "D Dominant 7th",
    "D Diminished 7th",

    "Eb Major Arpeggio",
    "Eb Minor Arpeggio",
    "Eb Dominant 7th",
    "Eb Diminished 7th",

    "E Major Arpeggio",
    "E Minor Arpeggio",
    "E Dominant 7th",
    "E Diminished 7th",

    "F Major Arpeggio",
    "F Minor Arpeggio",
    "F Dominant 7th",
    "F Diminished 7th",

    "F# Major Arpeggio",
    "F# Minor Arpeggio",
    "F# Dominant 7th",
    "F# Diminished 7th",

    "G Major Arpeggio",
    "G Minor Arpeggio",
    "G Dominant 7th",
    "G Diminished 7th",

    "Ab Major Arpeggio",
    "Ab Minor Arpeggio",
    "Ab Dominant 7th",
    "Ab Diminished 7th",

    "A Major Arpeggio",
    "A Minor Arpeggio",
    "A Dominant 7th",
    "A Diminished 7th",

    "Bb Major Arpeggio",
    "Bb Minor Arpeggio",
    "Bb Dominant 7th",
    "Bb Diminished 7th",

    "B Major Arpeggio",
    "B Minor Arpeggio",
    "B Dominant 7th",
    "B Diminished 7th"
]

masterlist = [Scales, Appregios]

yr2scaleslist = [
    "F Major Scale",
    "F Minor Harmonic",
    "F Minor Melodic",
    "F Chromatic",
    
    "F# Major Scale",
    "F# Minor Harmonic",
    "F# Minor Melodic",
    "F# Chromatic",
    
    "Ab Major Scale",
    "Ab Minor Harmonic",
    "Ab Minor Melodic",
    "Ab Chromatic",
    
    "Bb Major Scale",
    "Bb Minor Harmonic",
    "Bb Minor Melodic",
    "Bb Chromatic",
    
    "B Major Scale",
    "B Minor Harmonic",
    "B Minor Melodic",
    "B Chromatic"
]

yr2appregiolist = [
    "C Major Arpeggio",
    "C Minor Arpeggio",
    "C Dominant 7th",
    "C Diminished 7th",

    "F Major Arpeggio",
    "F Minor Arpeggio",
    "F Dominant 7th",
    "F Diminished 7th",

    "F# Major Arpeggio",
    "F# Minor Arpeggio",
    "F# Dominant 7th",
    "F# Diminished 7th",

    "Ab Major Arpeggio",
    "Ab Minor Arpeggio",
    "Ab Dominant 7th",
    "Ab Diminished 7th",

    "Bb Major Arpeggio",
    "Bb Minor Arpeggio",
    "Bb Dominant 7th",
    "Bb Diminished 7th",

    "B Major Arpeggio",
    "B Minor Arpeggio",
    "B Dominant 7th",
    "B Diminished 7th"
]

yr2list = [yr2scaleslist, yr2appregiolist]

#random generation
sran = random.item = random.choice(Scales)
aran = random.item = random.choice(Appregios)
#yr2
whichyr2 = random.item = random.choice(yr2list)
yr2play = random.item = random.choice(whichyr2)
#all
whichlist = random.item = random.choice(masterlist)
play = random.item = random.choice(whichlist)
#bowings
bowings = ["separate", "slurred", "spiccato"]
toabow = ["1 to a bow", "2 to a bow", "3 to a bow", "4 to a bow"]
bow = random.item = random.choice(bowings)

if bow == "spiccato":
    spiccbow = random.item = random.choice(toabow)
else:
    spiccbow = ""

#dropdown
option = st.selectbox(
    "Preset",
    ["Year 2", "All", "Scales only", "Appregios only", "Advanced..."],
    index=None
)

if option == "Year 2":
    randomlist = yr2play
elif option == "All":
    randomlist = play
elif option == "Scales only":
    randomlist = sran
elif option == "Appregios only":
    randomlist = aran
elif option == "Advanced...":
    option = st.multiselect("", (
    "C Major Scale",
    "C Minor Harmonic",
    "C Minor Melodic",
    "C Chromatic",
    "C Major Arpeggio",
    "C Minor Arpeggio",
    "C Dominant 7th",
    "C Diminished 7th",

    "C# Major Scale",
    "C# Minor Harmonic",
    "C# Minor Melodic",
    "C# Chromatic",
    "C# Major Arpeggio",
    "C# Minor Arpeggio",
    "C# Dominant 7th",
    "C# Diminished 7th",

    "D Major Scale",
    "D Minor Harmonic",
    "D Minor Melodic",
    "D Chromatic",
    "D Major Arpeggio",
    "D Minor Arpeggio",
    "D Dominant 7th",
    "D Diminished 7th",

    "Eb Major Scale",
    "Eb Minor Harmonic",
    "Eb Minor Melodic",
    "Eb Chromatic",
    "Eb Major Arpeggio",
    "Eb Minor Arpeggio",
    "Eb Dominant 7th",
    "Eb Diminished 7th",

    "E Major Scale",
    "E Minor Harmonic",
    "E Minor Melodic",
    "E Chromatic",
    "E Major Arpeggio",
    "E Minor Arpeggio",
    "E Dominant 7th",
    "E Diminished 7th",

    "F Major Scale",
    "F Minor Harmonic",
    "F Minor Melodic",
    "F Chromatic",
    "F Major Arpeggio",
    "F Minor Arpeggio",
    "F Dominant 7th",
    "F Diminished 7th",

    "F# Major Scale",
    "F# Minor Harmonic",
    "F# Minor Melodic",
    "F# Chromatic",
    "F# Major Arpeggio",
    "F# Minor Arpeggio",
    "F# Dominant 7th",
    "F# Diminished 7th",

    "G Major Scale",
    "G Minor Harmonic",
    "G Minor Melodic",
    "G Chromatic",
    "G Major Arpeggio",
    "G Minor Arpeggio",
    "G Dominant 7th",
    "G Diminished 7th",

    "Ab Major Scale",
    "Ab Minor Harmonic",
    "Ab Minor Melodic",
    "Ab Chromatic",
    "Ab Major Arpeggio",
    "Ab Minor Arpeggio",
    "Ab Dominant 7th",
    "Ab Diminished 7th",

    "A Major Scale",
    "A Minor Harmonic",
    "A Minor Melodic",
    "A Chromatic",
    "A Major Arpeggio",
    "A Minor Arpeggio",
    "A Dominant 7th",
    "A Diminished 7th",

    "Bb Major Scale",
    "Bb Minor Harmonic",
    "Bb Minor Melodic",
    "Bb Chromatic",
    "Bb Major Arpeggio",
    "Bb Minor Arpeggio",
    "Bb Dominant 7th",
    "Bb Diminished 7th",

    "B Major Scale",
    "B Minor Harmonic",
    "B Minor Melodic",
    "B Chromatic",
    "B Major Arpeggio",
    "B Minor Arpeggio",
    "B Dominant 7th",
    "B Diminished 7th"))
    randomlist = random.item = random.choice(option)
#randomlist -> button generation variable

if st.button("Generate!"):
    st.write(randomlist)
    st.write(bow, spiccbow)
