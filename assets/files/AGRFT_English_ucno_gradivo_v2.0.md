# English for Film and Television

**Course materials / Učno gradivo · Version 2.0**

**Author:** Damjan Popič  
**Edition:** 2.0 · 7 October 2026  
**Course:** Angleški jezik, Film and Television, second year, AGRFT, University of Ljubljana  
**Contact:** [damjan.popic@ff.uni-lj.si](mailto:damjan.popic@ff.uni-lj.si)

We begin with the equipment used to make and edit audiovisual work. Opening a computer lets us name its components and explain their functions. Following the signal leads from electricity and bits to digital sound, moving images and the camera. We then move onto the set: the people, responsibilities, instructions, documents and decisions through which a production works.

The first four chapters provide the technical foundations. They move from visible components to mechanisms, with schematics, numerical examples and English explanations. Read them alongside the lecturer's demonstration and return to the deeper examples as the course progresses. A drawing's caption identifies its scope: a functional connection, a mathematical model or a specified teaching circuit. Actual equipment must be interpreted through its own documentation.

The remaining chapters develop professional terminology, creative and technical explanation, correspondence, project presentation and post-production. The final section contains **105 individual exercises**, followed by answers and model responses. Oral work consists of explaining, presenting and answering the lecturer's questions. All exercise texts and calculation data are included; observation tasks use the demonstration or the indicated schematic.

Nick Ceramella and Elizabeth Lee's *Cambridge English for the Media* (2008) remains the main book reference for language and professional communication. Its printed page numbers are cited throughout the relevant chapters. The technical foundations draw on primary engineering and standards documentation identified beside the explanations. The worked examples, model texts, diagrams and exercises are original teaching material. Hypothetical hardware and production requirements are labelled as such.

### Studying and assessment

The course comprises 45 seminar hours. Assessment consists of **written work (50%)** and an **oral presentation (50%)**, developed through coursework. Both components must receive a positive grade; if either component is negative, the course assessment scheme requires the student to take an exam.

The final exercises explain how to prepare an individual written submission and oral presentation. The lecturer announces submission dates, presentation slots and any task-specific limits. Keep drafts and revised versions so that you can identify and explain improvements.

In written work, attend to purpose, audience, organisation, terminology, register and grammatical control. In oral work, attend to comprehensibility, organisation, appropriate terminology and the ability to clarify and answer a question. Use of a specialist term should help the listener understand your work. When a term is unfamiliar to the intended audience, explain it.

For email submissions and questions, use **AGRFT — English** followed by the exercise number or assignment title in the subject line. Include your name in the submitted file. Individual submissions and feedback use the course email.

### Using sources and this edition

Check unfamiliar terms in a reliable dictionary and in relevant professional documentation. Record the source of a technical definition or specification. Distinguish quotations from your own explanation. When using a language tool, check that the revision preserves your facts, uncertainty and terminology. An assessed text should contain language you understand and can explain; follow the lecturer's instructions on permitted tools and acknowledge substantive assistance.

The [current course page](https://damjan-popic.github.io/en/teaching/agrft/) is the reading version. The [editable Markdown source](https://github.com/damjan-popic/damjan-popic.github.io/blob/main/content/en/teaching/agrft.md) holds the complete teaching text. The [version 2.0 archive](https://github.com/damjan-popic/damjan-popic.github.io/blob/agrft-v2.0/content/en/teaching/agrft.md) preserves this edition; [version 1.0](https://github.com/damjan-popic/damjan-popic.github.io/blob/agrft-v1.0/content/en/teaching/agrft.md) remains available.

[Download the Markdown text](https://raw.githubusercontent.com/damjan-popic/damjan-popic.github.io/main/assets/files/AGRFT_English_ucno_gradivo_v2.0.md) or [download version 2.0 with all schematics](https://damjan-popic.github.io/assets/files/AGRFT_English_ucno_gradivo_v2.0.zip). The package contains one Markdown text and the eighteen SVG drawings it uses. Open a drawing's full-size link when studying its connections or using it for projection.

## 1. How computers work, deep down

A computer does not begin with an app. It begins with physical devices whose electrical states can be controlled and distinguished. Circuits use those states to represent bits; other circuits combine bits, retain them and move them. Instructions determine which operations happen. A video editor eventually presents the result as pictures, waveforms, buttons and a timeline.

This chapter follows that chain in both directions. Start with the parts visible inside a desktop computer, then examine the principles hidden inside the chips. Return to the complete machine by following a file from storage to the screen. The English task is to identify a part, explain its function, describe a connection and justify a diagnosis.

The system drawings are **functional schematics**, with their assumptions stated in the captions. They are not wiring instructions for a particular motherboard. The transistor circuit, Boolean tables, binary examples and teaching processor have explicitly defined behaviour. A laptop, an older desktop and a modern system on a chip can distribute the same functions differently.

### The opened computer: what are we looking at?

For the demonstration, shut the computer down, disconnect it from mains power and follow its service instructions before handling internal parts. Handle boards by their edges and use the appropriate precautions against electrostatic discharge. **Leave the power supply's own enclosure closed:** its capacitors can retain a dangerous charge after disconnection. Removing a computer's side panel and opening the power supply are different operations. See Corsair's [power-supply safety instructions](https://www.corsair.com/uk/en/explorer/diy-builder/power-supply-units/power-supply-manual/) and [explanation of stored charge](https://www.corsair.com/fr/hu/explorer/diy-builder/power-supply-units/can-i-open-up-my-power-supply/).

![Functional data paths in a representative desktop: CPU memory controller to DRAM, PCIe to discrete GPU and NVMe SSD, platform link to chipset and additional I/O. Power is described separately.](https://damjan-popic.github.io/assets/images/agrft/v2/computer-system.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/computer-system.svg)

*Read the arrows as data connections. Power distribution is shown separately. This is a representative desktop with a CPU memory controller, a discrete graphics card and an I/O chipset. Some computers integrate the GPU, memory or more I/O functions in the processor package.*

Use the following vocabulary while looking at the actual machine. A component's colour is not a reliable identifier; use its construction, label, connector and relationship to neighbouring parts.

| Part | What it does and how to identify its function | Slovene orientation |
| --- | --- | --- |
| **case / chassis** | Mechanically supports and protects the assembly. Mounting points, panels and airflow openings belong to the case; it does not execute the program. | ohišje |
| **motherboard / mainboard** | Carries integrated circuits, connectors and conductive paths linking the system. Its layers distribute electrical signals, power and ground. | matična plošča |
| **printed circuit board / PCB** | An insulating board with patterned conductors and mounted components. The motherboard, graphics card and SSD can each have a PCB. | tiskano vezje |
| **trace; via** | A trace is a patterned conductor on a board layer; a via connects conductors between layers. A visible line is part of an electrical connection, not a miniature conveyor belt of complete files. | vez; prehod med plastmi |
| **CPU / central processing unit** | Executes the machine instructions of programs. The visible package contains one or more semiconductor dies and connections to the board. | centralna procesna enota; procesor |
| **CPU socket** | Provides the specified mechanical and electrical connection for a compatible processor package. Many laptops use a soldered processor instead. | procesorsko podnožje |
| **die; package** | The die is a piece of semiconductor containing circuitry; the package protects and connects one or more dies. The metal surface under a cooler is not the exposed transistor array. | posamezen čip, izrezan iz polprevodniške rezine; ohišje čipa |
| **integrated heat spreader** | A conductive lid on some processor packages that spreads heat towards the cooler. It is not the cooler's fan. | pokrov za razporeditev toplote |
| **heat sink** | Conducts heat away from a component and exposes a larger surface to the surrounding air or cooling system. Its fins increase the available surface. | hladilno telo |
| **thermal interface material / thermal paste** | Reduces thermal resistance at the contact between mating surfaces by filling small gaps. It does not supply electrical power to the processor. | termalna pasta; toplotno prevoden vmesnik |
| **fan** | Moves air. A CPU fan, case fan and PSU fan serve different positions in the cooling path. A liquid cooler also uses a pump, coolant and a radiator. | ventilator |
| **power supply unit / PSU** | Converts mains input into regulated DC outputs suitable for the computer. Its wattage rating describes capacity, not a constant consumption. | napajalnik |
| **power connector** | Carries electrical power to a board or device. Physical fit does not prove electrical compatibility, particularly for modular PSU cables. | napajalni priključek |
| **voltage regulator module / VRM** | Uses switching devices, inductors and capacitors to provide the lower, regulated supply required by a processor or other component. | sklop za uravnavanje napetosti |
| **capacitor** | Stores energy in an electric field. Around a processor, capacitors help stabilise supply voltage during changing demand. | kondenzator |
| **inductor / choke** | Stores energy in a magnetic field and opposes rapid changes in current; part of many switching regulators. | tuljava; dušilka |
| **RAM / main memory** | Holds active program instructions and data so the processor can access them. Ordinary DRAM does not retain the contents without power. | delovni pomnilnik |
| **DIMM; SO-DIMM** | A memory module and its smaller counterpart. A module carries several devices and fits a compatible memory socket. Newer systems can use other module designs or soldered memory. | pomnilniški modul; manjši modul |
| **memory controller** | Coordinates reads, writes and timing for main memory. In many current desktops it is part of the processor. | pomnilniški krmilnik |
| **chipset / I/O hub** | Provides additional input/output connections and controllers. It links those devices to the processor through an upstream connection. | vezni nabor; vhodno-izhodno vozlišče |
| **PCIe slot** | Connects an expansion card to PCI Express links. A long physical slot does not by itself prove that all sixteen lanes are connected. | razširitvena reža PCIe |
| **graphics card** | An expansion board containing a GPU, usually its own memory, power circuitry, cooling and display outputs. | grafična kartica |
| **GPU / graphics processing unit** | Performs graphics and other suitably parallel computations. A GPU can be integrated into a processor instead of occupying a separate card. | grafični procesor |
| **VRAM / graphics memory** | Stores resources such as textures, working image buffers and GPU results. Separate graphics memory and system RAM are not automatically interchangeable. | grafični pomnilnik |
| **SSD / solid-state drive** | Persistent storage normally combining NAND flash, a controller and firmware. It contains no rotating recording platter. | polprevodniški pogon |
| **M.2 module and socket** | A physical module arrangement used for devices including SSDs. The form does not by itself establish whether a storage device uses SATA or PCIe/NVMe. | modul in priključek M.2 |
| **HDD / hard disk drive** | Uses magnetic recording surfaces on rotating platters, with heads positioned by an actuator. Mechanical movement affects access time. | trdi disk |
| **SATA data connector** | Carries a SATA data link. A typical internal SATA drive also needs a separate power connection. | podatkovni priključek SATA |
| **optical drive** | Uses a laser and optical detection to read supported disc structures; a writer can also record compatible media. | optični pogon |
| **firmware flash** | Non-volatile memory holding low-level code, such as platform firmware. The operating system normally resides elsewhere. | bliskovni pomnilnik vdelane programske opreme |
| **RTC battery** | Supports the real-time clock and, on some designs, battery-backed state when external power is absent. It does not power ordinary RAM or store all the firmware. | baterija ure realnega časa |
| **network adapter / NIC** | Implements network communication through a wired or wireless interface. It may be integrated, an expansion card or an external device. | omrežni vmesnik |
| **audio interface** | Provides audio input/output functions; it may contain preamps, ADCs, DACs and digital connections. Different interfaces contain different combinations. | zvočni vmesnik |
| **capture card** | Receives supported external video/audio signals and makes them available to the computer. A graphics card's output socket is not automatically a video input. | zajemalna kartica |
| **port; connector; header** | A port provides an interface; a connector is its physical connection; an internal header often connects case buttons, LEDs or front-panel ports to the board. | vmesnik oziroma vrata; priključek; priključni zatiči |

Intel's [motherboard guide](https://www.intel.com/content/www/us/en/gaming/resources/how-to-choose-a-motherboard.html) provides the architectural distinction between processor connections and chipset connections. Its [assembly guide](https://www.intel.com/content/www/us/en/gaming/resources/how-to-build-a-gaming-pc.html) illustrates the principal replaceable components. Particular sockets, lane counts and supported devices must be checked in the actual machine's manual.

A complete spoken description can be short:

> This is a DIMM, a module that carries the computer's main memory. It fits into a memory socket on the motherboard. The memory controller reads and writes the data held in its DRAM devices. Those contents are lost when power is removed.

Compare that with “This is the memory.” The longer explanation identifies the object, its location, its relationship and the kind of retention it provides.

### Power, signals and heat

**Voltage** is an electrical potential difference, measured in volts. **Current** is the rate of charge flow, measured in amperes. **Power** is the rate of energy transfer, measured in watts. For a DC example with constant values, power equals voltage multiplied by current.

A hypothetical circuit drawing 10 A at 1 V receives 10 W. That does not mean its individual logic inputs are each supplied with a ten-ampere “one”. Supply rails provide energy; signal connections convey changing electrical states. A ground connection provides a common reference and a return path. It is not a drain into which unwanted information disappears.

The PSU's outputs are further regulated on the boards. A processor's exact operating voltage and current depend on the device and operating state. They cannot be inferred from the 230 V mains supply or from the shape of the CPU socket. The circuit needs correctly regulated supplies before its states can be interpreted reliably.

When a logic node changes voltage, capacitances charge or discharge. That movement costs energy. A useful simplified estimate for CMOS switching power is:

**P ≈ α C V² f**

Here **α** represents switching activity, **C** an effective switched capacitance, **V** supply voltage and **f** the reference clock frequency; α counts the average 0-to-1 charging events per clock period. The model does not include every loss, including leakage. It nevertheless explains why increasing frequency and especially voltage can increase heat. At constant α, C and f, multiplying voltage by 1.1 multiplies this contribution by 1.21.

A cooler carries this heat away. If the cooling path is inadequate, a processor may reduce its operating rate or shut down. “The fan makes the CPU faster” skips the mechanism. A more accurate sentence is: “The cooling system can allow the processor to sustain its intended operating conditions.”

The physical switching model is developed in MIT's [CMOS notes](https://computationstructures.org/notes/cmos/notes.html). The numerical power examples here are illustrative calculations, not settings to apply to the demonstration computer.

### What a bit physically is

A **bit** is a binary digit: one of two distinguishable values, conventionally 0 and 1. A bit is an abstract value. Its physical representation depends on the system.

A logic circuit can represent it using voltage ranges. A DRAM cell retains charge. A flash device distinguishes threshold-voltage states. A hard drive detects an encoded magnetic pattern. A network link may recover bits from several possible signal levels and a timing reference. There is no single universal physical object called a bit.

For an explicitly invented logic family, suppose a receiver accepts 0–0.3 V as low and 0.7–1.0 V as high. Then 0.1 V and 0.2 V represent the same logical value; 0.8 V and 0.9 V represent the other. The gap is an undefined input region, not a third valid binary digit. Real voltage limits come from the relevant device specification.

This separation explains why digital information can survive modest physical variation. A receiver classifies an input and another circuit regenerates a suitable output level. Excess noise, incorrect timing or a failed device can still cause an error. “Digital” does not mean physically perfect.

Do not imagine a digital signal as mathematically vertical edges painted onto a wire. Real edges take time, can ring or overshoot, and propagate at finite speed. Binary interpretation is a rule applied to the physical signal.

### The transistor: from a voltage to a controlled path

A **transistor** is a semiconductor device that controls electrical behaviour. In a MOS field-effect transistor, a voltage on the **gate** influences a conducting channel between **source** and **drain**. The gate is separated from the channel by an insulating structure. The **body** or bulk is a fourth electrical terminal, often tied to an appropriate supply in the introductory circuit.

A transistor used for digital logic is not a miniature mechanical switch with moving contacts. Charge and electric fields alter conduction. Real devices have resistance, capacitance, leakage and operating limits. Contemporary transistor geometries differ from the flat classroom cross-section, but the controlled-channel principle remains useful.

![A static CMOS inverter with a pMOS pull-up to VDD, nMOS pull-down to ground, common input at both gates and common output at both drains. Settled truth states shown.](https://damjan-popic.github.io/assets/images/agrft/v2/computer-cmos.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/computer-cmos.svg)

*Static CMOS inverter. The p-channel transistor provides the pull-up path to VDD; the n-channel transistor provides the pull-down path to ground. Both gates receive A. Their drains meet at Y. Body connections to the respective rails and parasitic capacitances are omitted. This is a connectivity schematic, not a drawing of the manufactured geometry.*

In this circuit, a low input turns the p-channel path on and the n-channel path off. The output approaches the positive supply, which represents 1. A high input reverses the conducting paths and pulls the output towards ground, representing 0.

| Input A | Pull-up pMOS | Pull-down nMOS | Settled output Y |
| --- | --- | --- | --- |
| 0 | conducting | non-conducting | 1 |
| 1 | non-conducting | conducting | 0 |

“Off” here means the simplified switching state; a real device still has leakage. During a transition, the ideal table does not describe every instant. There can be a brief interval of simultaneous conduction, and the output needs time to settle. The gate's timing specifications matter.

The circuit implements **NOT**: Y is the opposite of A. A small electrical mechanism has now become a logical operation. Intel's [transistor explanation](https://newsroom.intel.com/tech101/the-transistor-explained) gives the device context; MIT's [device-level lecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s1/) explains the complementary pull-up and pull-down arrangement.

### Logic gates: decisions without understanding

A **logic gate** computes a Boolean function. A combinational circuit's settled output depends on its current input values. The terms **AND**, **OR** and **XOR** describe precisely defined functions, not approximate English meanings.

| A | B | AND | OR | XOR | NAND | NOR |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

**AND** is 1 when both inputs are 1. **OR** is 1 when at least one is 1. **XOR**, exclusive OR, is 1 when the inputs differ. NAND inverts AND; NOR inverts OR.

For a two-input static CMOS NAND, the pull-down has two nMOS devices in series. Both must conduct to connect the output to ground. Its complementary pMOS pull-up has parallel paths. If either input is low, at least one pull-up path conducts. This gives exactly the NAND column.

A gate does not know that one input represents “the door is closed” and another “recording is enabled”. Those meanings come from the surrounding design. The same truth table could combine status signals, bits of a number or intermediate results in a codec.

A **multiplexer**, or mux, selects one of several inputs according to a select value. A **decoder** activates an output associated with an input code. Neither term necessarily refers to a media codec. These circuits allow a processor to select operands and turn an instruction's bit fields into control signals.

MIT's [combinational-logic notes](https://computationstructures.org/notes/combinational_logic/notes.html) explain how truth tables and gate networks specify the same function.

### Binary numbers, bytes and interpretation

In ordinary decimal notation, each position has ten times the weight of the position to its right. In binary, each position has twice the weight. For an unsigned eight-bit quantity, the weights are:

| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Weight | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| Example bits | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |

The example is **8 + 4 + 1 = 13**. Eight bits give **2⁸ = 256** distinct patterns. Unsigned interpretation assigns them the integers 0–255. A **byte**, as used throughout this material, is eight bits. A **nibble** is four bits.

**Hexadecimal**, base sixteen, is a compact notation for binary patterns. Each hexadecimal digit represents four bits. Digits A–F stand for decimal values 10–15. Thus the byte 1010 0110 is A6 in hexadecimal and 166 when interpreted as unsigned decimal. The prefix **0x** often marks hexadecimal: 0xA6.

The same bits can support different interpretations:

| Pattern | Interpretation | Result |
| --- | --- | --- |
| 01000001 | unsigned integer | 65 |
| 01000001 | ASCII-compatible text code in UTF-8 | A |
| 01000001 | one unsigned component sample in a specified image | a code value of 65; displayed light depends on the colour representation |
| 11111111 | unsigned eight-bit integer | 255 |
| 11111111 | signed eight-bit two's-complement integer | −1 |

**Two's complement** assigns the most significant bit a negative weight. For eight bits, the weights are −128, 64, 32, 16, 8, 4, 2 and 1. Therefore 11111111 means −128 + 127 = −1. The range is −128 to +127. A sample's bit depth alone does not tell us whether it is signed or unsigned.

Text adds another layer. UTF-8 represents Unicode characters using sequences of one to four bytes. The precomposed character **č**, U+010D, is encoded as **C4 8D**. Its code-point value is 269, or 100001101 in binary. Padded to the eleven-bit field 00100001101, it fits the two-byte template 110xxxxx 10xxxxxx: 11000100 10001101. A character is therefore not always one byte. A visibly identical character can also be represented using a base letter followed by a combining mark, with a different byte sequence. See the Unicode Consortium's [UTF encoding explanation](https://www.unicode.org/faq/utf_bom.html).

Byte order matters when several bytes represent one quantity. The sixteen-bit unsigned number 0x1234 equals 4,660. In **little-endian** byte order, its low-address byte is 34 and the next is 12. In **big-endian** byte order, they are 12 and 34. The order of bytes in memory is a separate issue from writing the bits of a byte most significant first on the page.

Size and rate also need precise units:

| Unit | Meaning |
| --- | --- |
| 1 kB | 1,000 bytes |
| 1 MB | 1,000,000 bytes |
| 1 GB | 1,000,000,000 bytes |
| 1 KiB | 1,024 bytes |
| 1 MiB | 1,048,576 bytes |
| 1 GiB | 1,073,741,824 bytes |
| 1 Mb/s | 1,000,000 bits per second |
| 1 MB/s | 1,000,000 bytes per second, or 8 Mb/s |

The binary prefixes follow the [definitions explained by NIST](https://physics.nist.gov/cuu/Units/binary.html). A nominal 1 TB drive contains approximately 931.3 GiB before considering formatting and reserved space. This numerical difference does not by itself indicate missing files.

### How the computer adds

A **half adder** takes two input bits. Its sum bit is A XOR B; its carry is A AND B. For 1 + 1, the sum position becomes 0 and the carry becomes 1: binary 10.

A **full adder** also accepts an incoming carry. Its outputs are:

**S = A XOR B XOR Cin**

**Cout = (A AND B) OR (Cin AND (A XOR B))**

![Full adder Boolean circuit and a five-bit portion of an eight-bit ripple-carry example computing thirteen plus seven equals twenty.](https://damjan-popic.github.io/assets/images/agrft/v2/computer-adder.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/computer-adder.svg)

*The upper circuit implements one full adder using two XOR functions, two AND functions and one OR function. The lower example connects carry outputs to the next more significant bit. It is a ripple-carry teaching design; high-performance processors use more elaborate arrangements to reduce delay.*

| A | B | Cin | Sum S | Cout |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Follow **13 + 7** from the least significant position:

| Bit position | Bit of 13 | Bit of 7 | Carry in | Sum bit | Carry out |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 2 | 1 | 1 | 1 | 1 | 1 |
| 3 | 1 | 0 | 1 | 0 | 1 |
| 4 | 0 | 0 | 1 | 1 | 0 |
| 5–7 | 0 | 0 | 0 | 0 | 0 |

Read the eight sum bits in the usual most-significant-first order: **00010100**, or 20. Transistor networks implementing those gates can produce this result without recognising the English words *thirteen* or *seven*.

A fixed width limits the result. In eight-bit unsigned arithmetic, 255 + 1 produces low eight bits 00000000 and a carry out. In signed eight-bit arithmetic, 127 + 1 produces 10000000, which represents −128; this is signed overflow. A carry flag and a signed-overflow condition are different. Software must choose an appropriate representation and handle results outside its range.

The circuit and arithmetic here are original worked constructions from the stated truth tables. They show how a numerical operation reduces to reproducible local rules.

### Retaining a state: latches, flip-flops and clocks

A combinational circuit does not by itself remember its previous result. **Sequential logic** includes retained state. Feedback allows a circuit to remain in one of two stable configurations until an input changes it.

A **latch** is level-sensitive: while enabled, it can follow its input; when closed, it retains the state. An edge-triggered **flip-flop** captures a state around a specified transition of a clock. Several such bit positions can form a **register**. A register holding eight bits can retain one of 256 patterns.

![Positive edge D flip-flop with a timing diagram showing D sampled on rising clock edges and Q retained between edges, excluding real setup hold and propagation specifications.](https://damjan-popic.github.io/assets/images/agrft/v2/computer-state.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/computer-state.svg)

*An idealised positive-edge-triggered D flip-flop and timing example. At each marked rising edge, Q takes the D value, after a small propagation delay. D must meet setup and hold requirements. The diagram illustrates the rule; its drawn time intervals are not the timing specifications of a real chip.*

For a register, a **clock** provides timing events. At an event, a new result is retained; the combinational logic then works from that retained result towards the next one. The data must settle early enough before the receiving edge and remain stable for the required interval after it. These are **setup time** and **hold time**.

If these constraints are violated, the device may become **metastable**: it can take an unpredictable time to settle to a valid state. That is an electrical timing problem, not a new value halfway between the numbers 0 and 1. Inputs crossing between clock domains require appropriate synchronisation.

A processor rated at 3 GHz has a nominal cycle period of about 0.333 ns at that frequency. It does not necessarily finish exactly three billion program instructions each second. An instruction may need several internal steps; a modern design may also overlap or complete several instructions in a cycle. Clocks can vary with workload and operating conditions.

MIT's [sequential-logic lecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c5/c5s1/) defines the timing terms, while its [sequential-circuit notes](https://computationstructures.org/notes/sequential_logic/notes.html) develop storage and feedback.

### Where bits are held

**Memory** is not a single interchangeable box. Different mechanisms trade density, latency, bandwidth, cost, endurance and retention.

| Mechanism | What physically retains the information | Main consequence |
| --- | --- | --- |
| Register storage | A powered sequential circuit retains a logical state. | Very close to the computation, but limited in capacity. |
| SRAM | A typical cell uses cross-coupled inverters and access transistors; feedback sustains its state while powered. | Fast access, relatively large cell area; commonly used for caches. |
| DRAM | A typical cell uses an access transistor and a capacitor. The charge must be sensed and restored. | Dense working memory that needs refresh and loses ordinary retention without power. |
| NAND flash | Stored charge changes a cell's threshold voltage; sensing classifies it into allowed ranges. | Non-volatile storage with programming, erase and endurance constraints. |
| Magnetic disk | A recording layer retains magnetic patterns recovered by read-channel electronics. | Persistent storage with mechanical positioning and rotation. |
| Optical disc | Manufactured or recorded optical structures alter a detected signal. | Readout needs optics, tracking and decoding, with format-specific rules. |

![DRAM access transistor and capacitor functional circuit, SRAM cross-coupled inverter feedback core, and an illustrative two-bit NAND threshold-state distribution.](https://damjan-popic.github.io/assets/images/agrft/v2/computer-memory.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/computer-memory.svg)

*The DRAM panel shows a functional 1-transistor/1-capacitor cell and its sense/restore connection; it omits shared-array circuitry. The SRAM panel shows the feedback core of a cell and labels the access connections. The NAND panel represents threshold-state intervals rather than a transistor cross-section. These are different physical mechanisms for retaining recoverable information.*

For DRAM, the **wordline** controls the access transistor and the **bitline** connects the selected cell to sensing circuitry. A small stored charge affects a larger shared line. A sense amplifier resolves the small difference and restores the selected state. Charge leaks, so rows must also be refreshed. The capacitor is not a cup containing a fixed number of “one electrons”; the circuit distinguishes an electrical state within operating tolerances. Micron explains the [one-transistor DRAM principle](https://www.micron.com/about/blog/memory/dram/how-dram-changed-the-world).

SRAM's “static” means the state can persist while power is supplied without the periodic cell refresh used by DRAM. It does not mean non-volatile or energy-free. In the common six-transistor design, two inverters form the feedback core and two additional transistors provide access. Reading and writing still require control circuitry.

For NAND, more than two threshold ranges can encode several bits in one cell:

| Naming convention | Bits per cell | Required distinguishable states |
| --- | --- | --- |
| SLC | 1 | 2 |
| MLC, in common product terminology | 2 | 4 |
| TLC | 3 | 8 |
| QLC | 4 | 16 |

“MLC” can also be used broadly to mean more than one bit per cell; read the manufacturer's context. The count follows **states = 2^(bits per cell)**. Four bits are not four miniature capacitors stacked inside one QLC cell. The controller maps a sixteen-way physical classification to a four-bit value.

Programming changes the stored charge. Erasing operates on larger groups than an individual byte. An SSD controller maps logical addresses to physical locations, manages spare space and wear, and applies error correction. A rewritten file need not return to the same cells. Micron's [NAND selection guide](https://www.micron.com/products/storage/nand-flash/choosing-the-right-nand) distinguishes the cell families; its [memory education presentation](https://www.micron.com/content/dam/micron/educatorhub/intro-to-memory/micron-intro-to-memory-presentation.pdf) illustrates threshold-state distributions.

An HDD instead positions heads over rotating platters. Data recovery involves sensing and decoding recorded patterns, with error correction; it is not a camera photographing printed zeros and ones. A random read may require positioning and waiting for rotation, while a long sequential read can amortise that work. See Seagate's [description of magnetic and solid-state storage](https://www.seagate.com/innovation/hard-drives-and-ssds/).

A storage medium's persistence also has limits. A file remaining after a normal shutdown does not imply guaranteed indefinite survival. For production material, retention, redundancy, independent backup and verified copying are separate requirements.

### Addresses, caches and virtual memory

An **address** identifies a location in an address space. In a byte-addressable model with eight address bits there are 256 possible byte addresses, 0–255. That model can address 256 bytes, not 256 bits. Thirty-two address bits can distinguish 2³² byte locations, or 4 GiB. This arithmetic does not prove that a particular processor or operating system exposes its entire theoretical address space as installed RAM.

A **cache** holds copies of selected data closer to the computation. If the requested information is present, there is a **cache hit**. If it must be obtained from the next level, there is a **cache miss**. Real caches transfer and track blocks called **cache lines** rather than independently managing every byte.

Suppose a program processes neighbouring samples in order. After it reads one sample, nearby samples are likely to be useful. This is **spatial locality**. Reusing a coefficient many times gives **temporal locality**. Both explain why a relatively small cache can reduce traffic to slower memory. Registers, L1/L2/L3 caches and main memory have different roles; exact levels and sharing arrangements depend on the processor. See MIT's [memory-hierarchy lecture](https://computationstructures.org/lectures/caches/caches.html).

**Virtual memory** maps a program's addresses to physical memory under hardware and operating-system control. A **memory management unit / MMU** performs address translation and access checks; a **translation lookaside buffer / TLB** caches translations. Pages can be backed by files or by other storage, and the operating system can move some contents when necessary. Virtual memory is broader than “using the SSD as extra RAM”. Protection and controlled address spaces are central functions. MIT's [virtual-memory lecture](https://computationstructures.org/lectures/vm/vm.html) develops the distinction.

In an editing system, insufficient RAM can cause repeated loading, eviction or paging. Buying a large SSD increases persistent capacity; it does not give it DRAM's access properties. Conversely, adding RAM will not solve every slow export. The slowest relevant stage has to be identified.

### A processor we can trace completely

A **CPU core** contains working state, arithmetic and logic circuits, control mechanisms and connections to memory. Its **instruction set architecture / ISA** defines the visible operations and their meaning. The hardware implementation can change while retaining the same architectural behaviour. MIT's [processor-design lecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c9/c9s1/) establishes this relationship.

For an exact classroom example, define the following small machine. **It is an invented teaching processor, not x86, Arm or RISC-V.** Its rules are deliberately complete enough to trace the program below.

- Memory contains 256 byte locations, addressed from 0x00 to 0xFF.
- An eight-bit **accumulator**, A, holds the current arithmetic value.
- An eight-bit **program counter**, PC, holds the address of the next instruction.
- Each instruction occupies two bytes. The first byte contains a four-bit opcode followed by four reserved zero bits. The second contains an eight-bit operand.
- Instructions begin at even addresses. For the program shown, PC starts at 0x00 and A at 0.
- After completing a non-halting instruction, PC increases by two. This machine would wrap PC modulo 256; this program does not approach that boundary.
- Arithmetic retains the low eight bits, that is, results modulo 256. No carry flag is exposed.
- An instruction register retains the two fetched bytes while the instruction executes.

| First byte | Mnemonic | Meaning of the second byte |
| --- | --- | --- |
| 00010000 / 0x10 | LDI | Immediate value to load into A. |
| 00100000 / 0x20 | ADDI | Immediate value to add to A. |
| 00110000 / 0x30 | STA | Byte address at which to store A. |
| 11110000 / 0xF0 | HALT | Must be 0x00 in this program; stop execution and leave PC at the HALT address. |

An **immediate** is a value encoded in the instruction itself. An **operand** is a value or reference on which an operation acts. The operand byte 0x80 in STA means an address; the operand byte 0x0D in LDI means the number 13. The opcode determines the interpretation.

The program is eight bytes long:

| Address | Byte in binary | Hexadecimal | Interpretation |
| --- | --- | --- | --- |
| 0x00 | 00010000 | 10 | LDI opcode |
| 0x01 | 00001101 | 0D | immediate 13 |
| 0x02 | 00100000 | 20 | ADDI opcode |
| 0x03 | 00000111 | 07 | immediate 7 |
| 0x04 | 00110000 | 30 | STA opcode |
| 0x05 | 10000000 | 80 | destination address 128 |
| 0x06 | 11110000 | F0 | HALT opcode |
| 0x07 | 00000000 | 00 | unused operand, fixed here to zero |

![Functional data paths of a fully specified teaching processor: PC or operand selects byte memory address, instruction register holds fetched bytes, decoder controls an ALU and accumulator, accumulator writes back to memory.](https://damjan-popic.github.io/assets/images/agrft/v2/computer-cpu.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/computer-cpu.svg)

*Functional datapath for the teaching processor. Thick data connections are eight bits unless marked otherwise; the instruction register retains sixteen bits. The control unit selects addresses, register updates, the ALU operation and memory writes. Real wiring needs control and timing signals as well as the depicted data routes.*

The execution trace is:

| Step | PC at instruction start | Action | A after action | Consequence |
| --- | --- | --- | --- | --- |
| 1 | 0x00 | Fetch 10 0D; decode LDI; retain operand in A. | 00001101 / 13 | PC becomes 0x02. |
| 2 | 0x02 | Fetch 20 07; decode ADDI; add operand to A. | 00010100 / 20 | PC becomes 0x04. |
| 3 | 0x04 | Fetch 30 80; decode STA; select address 0x80; write A. | 00010100 / 20 | Memory[0x80] becomes 0x14; PC becomes 0x06. |
| 4 | 0x06 | Fetch F0 00; decode HALT. | 00010100 / 20 | Execution stops; PC remains 0x06. |

**Fetch** obtains an instruction's bytes. **Decode** determines which controls their opcode requires. **Execute** performs the operation. **Write back** retains a result in the specified destination, when required. These are functional stages, not a promise of one clock cycle per stage.

What happens electrically during ADDI? The accumulator's stored bits drive one ALU input. The instruction's operand bits drive another. The adder's internal signals settle to the sum. A control signal permits the accumulator to capture that result at the appropriate clock event. The processor has not understood a sentence; a network has transformed and retained states according to its wiring and the instruction encoding.

If a byte changes, the effect depends on where it changes. Flipping the low bit of operand 0D makes it 0C, changing 13 to 12. Changing the opcode could select another operation or an undefined instruction. A change in an unused part of memory has no effect on this trace. “One wrong bit destroys everything” is as misleading as “one bit cannot matter”.

A **compiler** can translate a higher-level program into instructions for a target architecture. An **assembler** translates instruction mnemonics and their operands into machine code. A running interpreter is itself a program executing instructions while implementing the rules of another language. These layers do not remove the electrical foundation.

### What modern CPUs and GPUs add

Real processors add mechanisms that improve throughput while preserving the required program behaviour. A **pipeline** overlaps stages of different instructions. **Out-of-order execution** can perform ready work before earlier work has completed, while arranging the visible results appropriately. **Branch prediction** guesses a likely control-flow direction so useful work can begin sooner; a wrong guess can waste that work. Multiple **cores** can execute separate instruction streams.

These mechanisms are reasons to distinguish an architectural description from a transistor layout or a clock-by-clock implementation. A clock-frequency comparison alone cannot tell us which machine completes an editing task sooner. Work per cycle, memory behaviour, parallelism, instruction support, heat limits and the software implementation all matter. MIT's [pipeline lecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c15/c15s1/) provides a concrete model of overlapping instruction stages.

A GPU organises large amounts of arithmetic work across many execution resources. Applying a transformation to millions of image samples can expose considerable parallelism. A program with tightly dependent operations may expose much less. Moving data and synchronising results can also consume time. NVIDIA's [CUDA programming model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html) is one implementation-specific account, not a universal programming interface for all GPUs.

Graphics hardware can also contain **dedicated media engines**. A hardware video decoder is not simply the same thing as a collection of general GPU arithmetic cores. Codec, profile, level, bit depth, chroma format and hardware generation determine support. NVIDIA documents this separation in its [Video Codec SDK](https://developer.nvidia.com/video-codec-sdk?lang=en) and [NVDEC guide](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.1/nvdec-video-decoder-api-prog-guide/index.html).

A machine may therefore play one compressed file smoothly and struggle with another of similar resolution. The second may require software decoding, more complex dependencies or unsupported sample formats. The useful question is “Which operation is taking the time?” rather than simply “Is the GPU good?”

### Connections: shape, protocol and actual throughput

A **bus** or interconnect transfers information between components. Some connections carry bits in parallel; others send encoded symbols serially over high-speed links. Modern PCIe is a serial, packet-based, point-to-point interconnect. A lane contains separate transmit and receive paths, and links can combine lanes. Data does not pass through every component in a single universal circle.

| Distinction | What must be checked |
| --- | --- |
| **M.2 versus NVMe** | M.2 describes a physical module/connector arrangement. NVMe defines communication with non-volatile storage. A common desktop NVMe SSD uses PCIe, but NVMe also has other transports. |
| **PCIe slot length versus connected lanes** | Mechanical fit does not establish the negotiated electrical width, generation or lane sharing. |
| **USB-C versus USB data capability** | The connector shape does not establish supported speed, display transport, charging power or cable capability. |
| **HDMI/DisplayPort output versus capture input** | A display output sends a signal. Capturing an external signal requires a suitable input and receiving hardware. |
| **Gb/s versus GB/s** | Eight bits make a byte; protocol overhead, encoding and other work further reduce the useful file transfer rate. |
| **capacity versus bandwidth versus latency** | Capacity is how much can be held; bandwidth is a transfer rate; latency is the delay before an operation's result becomes available. |

The NVMe organisation's [specification overview](https://nvmexpress.org/specifications/) distinguishes protocol and transport. The USB Implementers Forum's [Type-C terminology guidance](https://www.usb.org/sites/default/files/usb_type-c_language_product_and_packaging_guidelines_20230320.pdf) explicitly separates the connector from the capabilities implemented with it.

An NVMe transfer illustrates the division of work. Host software prepares a command and buffer addresses; the controller reads the request, obtains the storage data and reports completion. **Direct memory access / DMA** allows devices to transfer data to or from memory without the CPU manually copying each byte through an arithmetic register. Drivers still arrange mappings, ownership and synchronisation. See the [NVMe queue overview](https://nvmexpress.org/base-nvm-express-part-one/) and the Linux kernel's [DMA guide](https://kernel.org/doc/html/v6.15/core-api/dma-api-howto.html).

Consider a hypothetical 100 GB media copy sustained at 250 MB/s. Ignoring setup and verification time:

**100,000 MB ÷ 250 MB/s = 400 s = 6 min 40 s.**

A 2,000 Mb/s stream also represents 250 MB/s before overhead. If several devices share an upstream link, their combined demand can exceed its useful throughput even when each device's own headline rate appears sufficient.

### From the power button to the editing application

The **power button** usually signals control circuitry; it is not necessarily a mechanical switch in series with every supply rail. Once the platform has established the required supplies and reset conditions, the processor begins at its defined startup location and executes firmware.

**Firmware** is software closely associated with a device or platform. Modern PCs commonly use **UEFI**, an interface framework for platform firmware and operating-system loaders. Firmware initialises sufficient hardware, discovers boot options and launches an appropriate loader. The loader starts the operating system. The [UEFI boot-manager specification](https://uefi.org/specs/UEFI/2.11/03_Boot_Manager.html) defines the boot-option mechanism; it does not prescribe the physical location of every chip on a motherboard.

The **operating-system kernel** manages resources and controlled access to hardware. **Device drivers** provide device-specific operations. The **scheduler** allocates processor time among runnable work. A **filesystem** organises names, directories, metadata and file contents on storage. The editing application runs within this environment.

The application executable is itself stored data. Starting it causes the necessary program pages and supporting resources to become available in memory. The machine then executes instructions from those pages. The difference between a program and a picture is therefore not that one contains bits and the other does not. Their formats and the operations applied to them differ.

A saved project file often contains edit decisions and references to media. It may not contain the original camera recordings. Moving the project without the referenced media can produce missing-file warnings. A **render cache** or **proxy** can make playback easier but does not necessarily replace the original material or the final export.

Operating systems can buffer file writes in memory before they reach persistent storage. The Linux kernel's [memory overview](https://docs.kernel.org/admin-guide/mm/concepts.html) explains page-cache and writeback behaviour. A finished progress animation is not a universal guarantee that every device has completed all persistent writes; follow the application's and operating system's safe-ejection procedure.

### Following one clip from the SSD to the screen

The following is a functional account of ordinary file playback. Direct-storage paths, unified-memory designs and particular applications can combine or bypass some transfers.

1. The application resolves the file through the filesystem and requests the required portions.
2. The storage controller retrieves encoded data. Transfers make those bytes available in buffers accessible to the software or relevant hardware.
3. A **demultiplexer** reads the container structure and separates packets belonging to video, audio and other streams.
4. A video **decoder** reconstructs image samples. Depending on the codec, it may need other pictures as references.
5. Processing applies the required scaling, colour conversion, effects and composition. CPU, GPU or dedicated hardware performs the supported operations.
6. A display path presents a frame buffer according to the display timing. The monitor converts the received image representation into controlled light.
7. Audio packets follow their own decoder, buffer, clocked output and DAC path, coordinated with the intended presentation timing.

The bytes read from the SSD are not normally identical to the bytes in the frame buffer. Decompression, colour conversion, resizing and composition can change both representation and amount of data. An audio waveform visible in the interface is a graphic derived from samples, not the electrical audio signal itself.

This distinction becomes visible in a worked size example. An uncompressed 1920 × 1080 image with four eight-bit components occupies:

**1920 × 1080 × 4 = 8,294,400 bytes**, approximately 7.91 MiB, before any row padding or extra structures.

At 25 such frames each second, one pass through those buffers represents **207,360,000 bytes/s**, or 207.36 MB/s. An effect that reads several frames and writes a result can require much more internal memory traffic than the compressed file's storage bit rate. Compression saves storage and transmission bandwidth while adding decoding work.

The same observation explains a common editing distinction: **playing**, **decoding**, **rendering**, **encoding** and **exporting** name related but different operations. Playing concerns timely presentation. Decoding recovers represented media from a coding scheme. Rendering produces a calculated result. Encoding creates a coded representation. Exporting packages and writes the chosen output, often involving all the preceding stages.

### Copying, checking and keeping the original

A byte-for-byte copy can preserve a file exactly. Re-encoding is a different operation. A lossless decode and re-encode can preserve the represented samples while producing a different file because compression choices or metadata differ. A lossy re-encode can change the samples themselves.

A **checksum** or cryptographic **hash** can help verify a copy. A SHA-256 digest has 256 bits, usually written as 64 hexadecimal characters. Compute the digest over the complete source and destination byte sequences and compare them. Matching strong hashes provide very high confidence of identical bytes; they do not show that the original recording was in focus, correctly exposed, synchronised or complete. NIST describes [cryptographic hash functions](https://csrc.nist.gov/glossary/term/Cryptographic_hash_function) and specifies SHA-256 in the [Secure Hash Standard](https://www.nist.gov/publications/secure-hash-standard).

**Error detection**, **error correction** and **backup** are different. Detection identifies evidence of a problem. Correction uses redundant information to recover some errors within a scheme's limits. Backup preserves another recoverable copy. A RAID arrangement that survives one drive failure is not automatically an independent backup of accidental deletions or unwanted edits.

For an original camera card, a professional handover should say what was copied, where it was copied, how it was verified and which source remains available. “I dragged the folder across” describes an action but leaves the state of the material uncertain.

> I copied the complete card structure to the project storage and to a separate backup destination. I compared the file hashes against the source. Both copies passed verification. The source card has not yet been cleared.

This is a model report, not a universal permission to erase a card. The production's agreed responsibility and backup procedure determine that decision.

### Explaining the machine in English

Technical explanations usually need a category, a mechanism and a consequence. Start with the visible object and move to the process:

> A heat sink is a cooling component. It conducts heat away from the processor and exposes a larger surface to moving air. If the thermal contact is poor, the processor may become too hot to sustain its operating rate.

> An SSD is a storage device. Its controller translates logical requests into operations on flash memory. It retains files without continuous power, whereas ordinary DRAM holds the active working data only while powered.

> The bytes identify a compressed video stream. The decoder reconstructs the image samples before the display system presents them. Changing the file extension does not perform that conversion.

| Purpose | Useful construction |
| --- | --- |
| Identify | “This is a …”; “The labelled component is …” |
| Locate | “It sits beneath …”; “It is mounted beside …”; “It plugs into …” |
| Describe function | “It stores …”; “It regulates …”; “It routes …”; “It converts … into …” |
| Describe connection | “It communicates with … through …”; “It receives … from …” |
| Explain a mechanism | “When …, the circuit …”; “The controller first …, then …” |
| State a consequence | “This allows …”; “As a result, …”; “The limiting factor is …” |
| Qualify the claim | “In this design …”; “For these settings …”; “The specification does not establish …” |
| Report a diagnosis | “The symptom is …”; “The test shows …”; “We have not yet established …” |

The computer demonstration can follow a manageable first pass: identify the power, processing, memory and storage parts; follow the functional connections; explain a voltage-coded bit; trace the inverter and addition; then follow a clip to the screen. The deeper circuit, memory and processor examples support subsequent explanation and individual study. Knowing the labels is the starting point. The goal is to explain what changes, what retains a state and what information is required to interpret it.

## 2. How digital sound works

A microphone, an audio file and a loudspeaker represent the same event in different ways. Air pressure moves a diaphragm. An electrical circuit represents that movement as a changing voltage. A converter produces numbers. A computer stores and processes those numbers. During playback, another converter and an amplifier produce the electrical signal that moves a loudspeaker.

Following that chain lets us answer a practical question precisely: **what changes when we change a recording setting, a file format, a cable or a piece of equipment?** The answer depends on where the change occurs. A higher recording bit depth cannot remove microphone overload. A lossless file cannot restore information discarded earlier. A correct sample rate does not, by itself, synchronise two independent recorders.

### Sound before it becomes data

Sound in air is a travelling variation in pressure. At a fixed point, pressure rises above and falls below the local equilibrium pressure. An audio waveform normally shows this variation over time; its negative values represent the opposite direction of variation, not “negative sound”.

For a simple sinusoidal example, write:

`p(t) = A × sin(2πft + φ)`

Here, `p(t)` is the pressure variation at time `t`, `A` is its peak amplitude, `f` is frequency in hertz, and `φ` is phase. One hertz means one cycle per second. A 1,000 Hz sine wave completes one cycle in 0.001 seconds, or 1 millisecond. Doubling its frequency halves its period.

A real voice contains many changing frequency components. Its waveform also contains an envelope: the slower pattern of attacks, sustained energy and decays. Frequency content helps determine timbre; frequency alone does not describe a voice. Amplitude and perceived loudness are related, but hearing also depends on frequency, duration and context.

Phase describes a position within a cycle relative to a reference. Two identical signals can reinforce each other when added in phase. If one is multiplied by −1, their sum is zero in the ideal example. Real microphones in different positions do not usually record perfectly identical signals, so polarity reversal does not cancel everything. A time delay produces different phase shifts at different frequencies; it is not generally equivalent to reversing polarity.

These distinctions explain why moving a microphone can change the sound even when the recorder settings remain identical. The acoustic signal reaching the diaphragm has changed.

**Reference:** Brüel & Kjær, [Sound and Vibration Handbook](https://www.bksv.com/downloads/svpockethandbook/index.html), for acoustic quantities and their measurement.

### Follow the signal through the system

![Acquisition chain microphone preamplifier analogue anti alias filtering ADC; PCM buffering encoding and storage; decoding and clocked DAC reconstruction amplification and loudspeaker playback.](https://damjan-popic.github.io/assets/images/agrft/v2/audio-chain.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/audio-chain.svg)

The schematic represents functional stages. Several stages may be integrated into one chip or device. A USB microphone, for example, contains an analogue microphone element and electronics as well as a digital interface.

| Stage | Input | What the stage does | Output |
| --- | --- | --- | --- |
| Microphone transducer | Sound pressure | Converts mechanical movement into an electrical signal | Analogue voltage |
| Preamplifier | Small microphone signal | Applies gain and presents a suitable signal to later circuitry | Larger analogue voltage |
| Anti-alias filtering | Analogue signal with unwanted high-frequency content | Restricts the bandwidth entering the sampling system | Band-limited analogue signal |
| Analogue-to-digital converter, ADC | Analogue voltage and a timing reference | Samples and quantises a representation of the signal | Digital sample values |
| Digital processing | Samples | Performs arithmetic such as gain, mixing and filtering | New samples |
| Encoder and file writer | Samples and metadata | Optionally compresses the audio and packages it | A stored file or transmitted stream |
| Decoder | Encoded audio | Recovers the sample representation specified by the codec | Samples for processing or playback |
| Digital-to-analogue converter, DAC | Samples and a timing reference | Produces an electrical representation of the sample sequence | Analogue signal, requiring reconstruction filtering |
| Power amplifier | Analogue signal | Supplies enough voltage and current to drive the load | Electrical power delivered to a loudspeaker |
| Loudspeaker | Electrical signal | Moves a diaphragm and generates pressure variations | Sound in air |

“Digital” identifies the representation at a stage. It does not mean the whole physical system has become independent of analogue behaviour. Converters need accurate voltages and timing; loudspeakers still move air.

A useful English explanation follows the connection: **“The preamplifier raises the microphone signal so that the converter can represent it at a suitable level.”** This is more informative than “the preamp makes the sound better”.

### Inside the microphone and audio interface

In a moving-coil dynamic microphone, a diaphragm moves a coil in a magnetic field. This motion generates a voltage. In a condenser microphone, diaphragm movement changes a capacitance; associated electronics turn that change into a usable signal. A condenser microphone requires an appropriate power source, but its powering arrangement depends on the design. “Condenser”, “directional” and “wireless” describe different properties: transducer type, pickup behaviour and connection method.

Microphone sensitivity relates electrical output to a stated acoustic input. Maximum sound-pressure level describes an operating limit under specified distortion conditions. A polar pattern describes sensitivity to direction, usually with frequency-dependent behaviour. These are separate specifications. A microphone can have a narrow pickup pattern and still record an unwanted source located in that direction. [Shure, microphone fundamentals](https://www.shure.com/en-US/docs/education/Microphone-Techniques-for-Recording).

An audio interface commonly contains input protection, microphone preamplifiers, converters, clocks, digital routing and output amplifiers. The input gain control acts at a particular location in that design. A software fader may act later on already digitised samples. Turning that fader down cannot undo distortion that occurred before conversion.

Connector names also require care. **XLR** describes a connector family; an XLR connector alone does not prove that a signal is analogue microphone audio. A **balanced** connection uses two signal conductors and a differential receiver to reject interference appearing similarly on both. A stereo headphone connection also has multiple conductors, but that does not make it a balanced mono connection. **USB** identifies a digital connection system; it does not guarantee a particular converter quality.

Read the actual labels: *mic input, line input, instrument input, headphone output, digital input, clock input*. A microphone output and a powered loudspeaker output serve different electrical purposes. The shape of a plug is insufficient evidence of compatibility. [Analog Devices, common-mode signals](https://www.analog.com/en/resources/glossary/common-mode-signals.html).

### Sampling: choosing when to measure

The sample rate tells us how many sample instants occur per second, **per channel**. At 48 kHz, each channel has 48,000 samples per second:

`sample interval = 1 / 48,000 s ≈ 20.833 microseconds`

Stereo does not turn a 48 kHz recording into a 96 kHz recording. It produces two values at each sample instant. We call the collection of simultaneous channel values a **sample frame**.

A sample is a value associated with an instant. It is not a tiny audio clip occupying the gap before the next sample. To reconstruct a signal from samples, we also need a bandwidth restriction. For ordinary baseband audio, the signal bandwidth must lie below half the sample rate. This boundary is the **Nyquist frequency**.

At 48 kHz, that boundary is 24 kHz. At 44.1 kHz, it is 22.05 kHz. Real filters need a transition region; the usable passband cannot simply be assumed to reach an ideal vertical cutoff at the boundary. Exactly two samples per sine-wave cycle also leaves a phase-dependent boundary case: a 24 kHz sine sampled at 48 kHz precisely at its zero crossings yields only zeros. [Walt Kester, Analog Devices MT-002](https://www.analog.com/media/en/training-seminars/tutorials/MT-002.pdf).

![Mathematically plotted thirty-kilohertz and eighteen-kilohertz cosines sampled at forty-eight kilohertz from zero to two hundred fifty microseconds. All thirteen sample dots coincide.](https://damjan-popic.github.io/assets/images/agrft/v2/audio-sampling.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/audio-sampling.svg)

Consider the plotted example. A 30 kHz cosine and an 18 kHz cosine have identical values at the sample instants of a 48 kHz system:

`cos(2π × 30,000 × n/48,000) = cos(2π × 18,000 × n/48,000)`

The equality holds for every integer sample index `n`. The samples alone cannot identify which continuous signal produced them. This ambiguity is **aliasing**. An unwanted 30 kHz input can appear as an 18 kHz component in the reconstructed audio. Filtering it after the alias has entered the audible band cannot distinguish it from a genuine 18 kHz component. The input must be appropriately filtered before sampling.

A higher sample rate can accommodate a wider bandwidth and affect processing requirements. It does not automatically make a correctly captured signal sound better. Ask what bandwidth the microphone, source, processing and delivery actually require.

### Quantisation: choosing a numerical value

Sampling makes time discrete. **Quantisation** assigns an amplitude to one of a finite set of representable values. **Linear PCM**, pulse-code modulation, uses equally spaced amplitude values. Sample rate and bit depth therefore answer different questions: *when are values recorded?* and *which values can be represented?*

An `N`-bit integer word has `2^N` possible patterns. Common signed representations use two’s complement:

| Integer bit depth | Number of possible values | Signed integer range |
| --- | ---: | ---: |
| 8 | 256 | −128 to +127 |
| 16 | 65,536 | −32,768 to +32,767 |
| 24 | 16,777,216 | −8,388,608 to +8,388,607 |

This table describes signed integers. Some audio formats, including conventional 8-bit PCM WAVE, use unsigned values instead. A file specification determines the interpretation. [Microsoft, audio devices and data types](https://learn.microsoft.com/en-us/windows/win32/multimedia/devices-and-data-types).

For a worked 16-bit example, define a normalised value as `integer / 32,768`. The endpoints are −1 and approximately +0.9999695. If the desired value is 0.1, scaling gives 3,276.8. Rounding to 3,277 and converting back gives approximately 0.1000061. The quantisation error in this example is about +0.0000061.

The **least significant bit**, LSB, has the smallest numerical weight. Increasing integer bit depth makes the spacing between amplitude codes smaller for the same full-scale range. It does not add more samples in time.

For an ideal uniform quantiser and a full-scale sine wave under the usual uncorrelated-error assumptions, the theoretical signal-to-quantisation-noise ratio is approximately:

`SNR = 6.02 × N + 1.76 dB`

This gives about 98 dB for 16 bits and 146 dB for 24 bits. These are model results, not promises about a recorder. Analogue noise, distortion, converter design and operating bandwidth limit real performance. A 24-bit output word does not establish 24 effective bits of measurement accuracy. [Kester, MT-001](https://www.analog.com/media/en/training-seminars/tutorials/MT-001.pdf).

### How a converter makes bits

An ADC is an electronic measurement system. It compares an input with a reference and uses circuitry to produce a digital result. There are several architectures; “the ADC” is not one universal circuit.

A **successive-approximation** converter gives an accessible example. It holds an input voltage, tries an internal DAC value, and asks a comparator whether the input is above or below that value. Control logic keeps or clears a trial bit, then tests the next bit. A simplified four-bit converter with a 1 V reference can work as follows. For this illustration, code `k` represents `k/16` volts, with lower-edge decisions:

| Trial for a held input of 0.70 V | Trial value | Decision |
| --- | ---: | --- |
| Set the 8-weight bit: `1000` | 0.5000 V | Keep it |
| Also set the 4-weight bit: `1100` | 0.7500 V | Clear the 4-weight bit |
| Also set the 2-weight bit: `1010` | 0.6250 V | Keep it |
| Also set the 1-weight bit: `1011` | 0.6875 V | Keep it |

The result is `1011`, decimal 11. This deliberately simple example uses truncating thresholds, so it is not the earlier nearest-value rounding model. Actual transfer functions specify their thresholds and errors. The key connection is physical: a comparator’s decision becomes a bit held by digital logic. [Kester, MT-021](https://www.analog.com/media/en/training-seminars/tutorials/MT-021.pdf).

Many audio converters use **delta-sigma** architectures. An internal modulator operates at a much higher rate than the eventual PCM output, uses feedback and noise shaping, and feeds digital filtering and decimation. **Decimation** means filtering and reducing the sample rate. It does not mean discarding arbitrary samples without considering their frequency content. Delta-sigma designs can use one-bit or multibit internal quantisers. The output file may still contain ordinary 24-bit PCM. [Kester, MT-022](https://www.analog.com/media/en/training-seminars/tutorials/MT-022.pdf).

For a concrete chip, Texas Instruments’ PCM1808 documentation identifies analogue filtering, delta-sigma modulation, digital decimation and a serial interface. Its specified 24-bit output and its measured signal-to-noise specification describe different properties. A chip diagram is evidence for that particular device, not for every sound card. [Texas Instruments, PCM1808](https://www.ti.com/product/PCM1808).

### From a sample value to bytes in a file

A computer stores bit patterns. The file format tells software how to interpret them. Take two simultaneous signed 16-bit values:

| Channel | Decimal value | Hexadecimal word | Binary word |
| --- | ---: | --- | --- |
| Left | +1,000 | `03E8` | `00000011 11101000` |
| Right | −1,000 | `FC18` | `11111100 00011000` |

To obtain the two’s-complement pattern for −1,000 in 16 bits, subtract 1,000 from 65,536. The result is 64,536, or hexadecimal `FC18`. The same pattern interpreted as an unsigned integer would mean +64,536. Bits carry no signedness label on their own.

For this example, specify **little-endian, interleaved, signed 16-bit PCM**, with left followed by right. Little-endian storage places the less significant byte first. The four stored bytes are:

`E8 03 18 FC`

That is one stereo sample frame. The following frame adds another four bytes. At 48 kHz, 48,000 such frames represent one second. In a big-endian representation, those same two values would be stored as `03 E8 FC 18`. Correctly decoded, both arrangements represent identical sample values.

Byte order is not playback quality. Incorrect byte-order interpretation is a decoding error. Nor should we infer that all PCM uses the same order: the L16 RTP payload, for example, specifies network byte order, with the most significant byte first. [IETF, RFC 3551, §4.5.11](https://www.rfc-editor.org/rfc/rfc3551.html#section-4.5.11).

A raw stream also needs its sample rate, channel count, word size and layout specified externally. A WAVE file supplies format information in chunks. The reader locates the audio data rather than treating every byte in the file as a sample. Artwork, names and timestamps are metadata, not extra sound.

### Calculate the data rate before choosing storage

For uncompressed, byte-packed integer PCM:

`bit rate = sample rate × bits per sample × number of channels`

`audio payload bytes = bit rate × duration in seconds / 8`

These calculations exclude headers, metadata, padding and other overhead. They also assume that 24-bit samples occupy three bytes; some systems carry 24 valid bits in a 32-bit slot.

| Recording | PCM bit rate | Payload per minute | Payload per hour |
| --- | ---: | ---: | ---: |
| 44.1 kHz, 16-bit, stereo | 1,411,200 bit/s | 10,584,000 B | 635,040,000 B |
| 48 kHz, 24-bit, mono | 1,152,000 bit/s | 8,640,000 B | 518,400,000 B |
| 48 kHz, 24-bit, stereo | 2,304,000 bit/s | 17,280,000 B | 1,036,800,000 B |
| 48 kHz, 24-bit, eight channels | 9,216,000 bit/s | 69,120,000 B | 4,147,200,000 B |
| 96 kHz, 24-bit, stereo | 4,608,000 bit/s | 34,560,000 B | 2,073,600,000 B |

Eight channels do not necessarily mean eight people. A recorder may capture isolated microphones, a production mix and other feeds. Count the recorded channels.

A ten-minute 48 kHz, 24-bit stereo recording contains 172,800,000 audio-data bytes: **172.8 MB** using decimal megabytes, or approximately **164.79 MiB** using 1,048,576 bytes per mebibyte. State which unit you mean.

At a constant encoded rate of 192 kbit/s, ten minutes needs 14,400,000 encoded-data bytes before overhead. That is a different calculation: we use the codec’s resulting bit rate, not a notional PCM bit depth. **192 kbit/s is not 192 kHz.** The first is data per second; the second is samples per second per channel.

Microsoft’s [WAVEFORMATEX documentation](https://learn.microsoft.com/en-us/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) formalises the relationship among channel count, sample size, block alignment and average byte rate for PCM.

### Processing sound is arithmetic with a deadline

A digital audio workstation, or DAW, reads sample values and computes new ones. If a gain factor is `g`, a basic gain operation is `y[n] = g × x[n]`. Mixing two aligned signals can be written `y[n] = x₁[n] + x₂[n]`. A delay of `D` samples produces `y[n] = x[n − D]`.

At 48 kHz, a delay of 480 samples is 10 milliseconds. At 96 kHz, the same sample count is 5 milliseconds. The number of samples and the duration are connected by the sample rate.

A simple three-sample averaging filter is `y[n] = (x[n] + x[n−1] + x[n−2]) / 3`. It smooths rapid changes, although it is not a complete professional equaliser. This example shows why filtering requires neighbouring values, stored state and arithmetic. A plug-in can contain many such operations and more elaborate algorithms.

Software usually works on **buffers** of samples. A buffer of 256 sample frames at 48 kHz spans approximately 5.333 milliseconds. That is one buffer’s duration, not automatically the total monitoring latency. Input and output buffers, converters, operating-system scheduling and plug-in lookahead can add delay.

A buffer underrun occurs when the playback system runs out of required data at the deadline. More RAM or a faster processor may help a particular bottleneck, but neither changes the acoustic waveform’s sample rate by itself. The component lesson now has a practical application: memory holds buffers; the processor executes the calculations; the audio device consumes or produces samples according to its clock.

### Dither and the limits of rounding

Reducing integer bit depth requires another quantisation. Simply truncating or rounding a quiet, regular signal can produce an error related to that signal. That error may be heard as distortion rather than as a steady noise floor.

**Dither** is deliberately added low-level noise used during quantisation to change the statistical behaviour of the error. Correctly chosen dither trades signal-dependent artefacts for a controlled noise floor. It also allows low-level information to influence the statistical pattern of output samples. A signal smaller than one LSB need not become a permanent, absolute silence.

**Noise shaping** redistributes noise over frequency. It is a separate operation from adding dither. A shaped-dither option normally combines the two, with consequences for the resulting noise spectrum.

Apply a suitable dither process when reducing precision to a final integer deliverable, following the software’s conversion behaviour. Adding independent dither repeatedly increases noise. Copying an unchanged integer file or losslessly encoding its sample sequence does not require a fresh dither pass. A DAW’s internal floating-point processing and its final integer export are separate stages. [Audacity Manual, Dither](https://manual.audacityteam.org/man/dither.html).

**Model explanation:** “The export reduces the word length from the processing format to 16-bit integer PCM. Dither controls the resulting quantisation error. It does not recover frequencies removed by an earlier encoder.”

### Levels: dBFS, dB SPL, true peak and loudness

A decibel expresses a ratio. A reference is essential. For an amplitude ratio, `20 × log₁₀(A₂/A₁)` gives the difference in decibels when the relevant conditions are held constant. Doubling amplitude gives approximately +6.02 dB; halving it gives approximately −6.02 dB.

| Term | What it describes | What it does not establish |
| --- | --- | --- |
| dB SPL | Acoustic pressure level relative to 20 micropascals in air | The numerical level in a file |
| dBFS | Digital level relative to a defined full-scale reference | Loudspeaker sound pressure in the room |
| Sample peak | Largest stored sample magnitude | Every possible peak between sample instants |
| dBTP / true peak | Estimate of reconstructed signal peaks relative to full scale | Programme loudness |
| LUFS | Loudness measurement relative to full scale using a defined algorithm | A universal delivery target |
| Headroom | Margin between the operating level and a relevant limit | Additional resolution that repairs existing overload |

With the acoustic reference above, 1 pascal RMS corresponds to approximately 94 dB SPL. Playing a file more quietly changes the acoustic output without changing its stored samples. There is no universal conversion from a file’s dBFS value to room dB SPL without a calibrated playback chain. [Brüel & Kjær, measurement definitions](https://www.bksv.com/downloads/svpockethandbook/index.html).

Integer PCM has a finite range. If a system replaces values outside its range with the extreme values, it **clips**. A clipped waveform contains distortion; reducing its level afterwards makes the distorted waveform quieter. An intersample peak can also exceed the largest stored sample, which explains the use of true-peak measurement.

For one concrete broadcast reference, EBU R 128 specifies a programme-loudness framework centred on −23 LUFS. Its associated guidance addresses true-peak limits and production practice. These figures belong to that delivery framework; they are not a universal target for every film, music master, online platform or classroom recording. [EBU R 128](https://tech.ebu.ch/publications/r128); [EBU Tech 3343](https://tech.ebu.ch/docs/tech/tech3343.pdf).

### Floating point and recoverable numerical overload

A 32-bit floating-point sample uses a different representation from a 32-bit integer. IEEE binary32 divides the stored word into a sign bit, eight exponent bits and 23 fraction bits. Normalised finite values have an implicit leading significand bit. This gives approximately 24 bits of significant binary precision over a very wide range of magnitudes; it does not give uniformly spaced 32-bit integer precision throughout that range.

Audio software commonly treats ±1.0 as its nominal full-scale reference, while floating-point arithmetic can represent values beyond it. Suppose two tracks each contain the value 0.75 at one instant. Their sum is 1.5. A floating-point mix can retain 1.5. Multiplying it later by 0.5 gives 0.75 again. If an earlier integer stage clipped the sum to its maximum instead, the original 1.5 would already have been lost.

A recorder that captures floating-point files needs suitable analogue and converter hardware to use the available numerical range. Some designs combine converter paths at different gains. The file format cannot prevent a microphone diaphragm, microphone electronics, input stage or wireless transmitter from overloading. Nor does renaming or converting a previously clipped file make it recoverable. [Sound Devices, Understanding 32-bit Float](https://support.sounddevices.com/hc/en-us/articles/41709146697243-Understanding-32-bit-Float); [How a 32-bit Float File Is Recorded](https://support.sounddevices.com/hc/en-us/articles/44084281511963-How-is-a-32-Bit-Float-File-Recorded).

Before integer export, bring the actual signal into the permitted range and check the destination requirements. Floating-point working headroom and final delivery headroom serve different purposes.

### Playback: the waveform is not a staircase

A graph that connects samples with horizontal steps is one way to display numbers or illustrate a sample-and-hold output. It is not a universal picture of the acoustic waveform delivered by a digital system.

Ideal reconstruction of a band-limited signal uses contributions from the sample sequence together. Mathematically, this can be expressed with shifted sinc functions. A useful reading of the formula is: **each sample contributes to a continuous reconstructed waveform; the contributions overlap**. It does not mean the DAC guesses freely at whatever happened between samples.

Practical DACs often interpolate digitally to a higher internal rate. Conversion produces an analogue electrical signal, and analogue reconstruction filtering suppresses unwanted high-frequency images. Real filters approximate the ideal operation within design limits. The final pressure waveform is continuous in time. Neither the loudspeaker nor the listener receives a sequence of isolated numerical points. [Kester, MT-017](https://www.analog.com/media/en/training-seminars/tutorials/MT-017.pdf).

The playback clock matters because it determines when sample values are converted. Short-term timing variation at conversion is called **jitter**. Network packet-arrival variation is also called jitter, but packets can be buffered before a separate playback clock consumes the samples. These are different locations in the chain.

For a lecturer demonstration, a sine wave shown both as sample markers and as a reconstructed waveform is more useful than a staircase alone. Label the axes and identify whether the display shows samples, an intermediate electronic output, or the reconstructed signal. [Xiph.Org, Digital Show & Tell](https://xiph.org/video/vid2.shtml) provides a technically focused demonstration resource.

### How an audio CD stores sound

A standard audio CD carries two-channel, 44.1 kHz, 16-bit linear PCM. It is a digital audio disc, but it does not store an ordinary folder of WAVE files. **Ripping** extracts its audio data and writes that data into a chosen file representation. A data CD containing MP3 files uses a different organisation and requires a player that understands it.

![CD-DA layered arithmetic: stereo sixteen-bit forty-four-point-one kilohertz PCM, logical 2352-byte audio blocks at 75 per second, and CIRC EFM physical frames of 588 channel bits at 7350 per second.](https://damjan-popic.github.io/assets/images/agrft/v2/audio-cd.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/audio-cd.svg)

Keep three uses of “frame” separate:

| Unit | Audio represented | Rate during normal playback |
| --- | --- | ---: |
| Stereo sample frame | One 16-bit left value and one 16-bit right value: 4 bytes | 44,100 per second |
| Small CD channel frame | Carries the equivalent of 24 audio-data bytes before physical-layer overhead | 7,350 per second |
| CD audio sector / logical audio block | 2,352 audio-data bytes: 588 stereo sample frames | 75 per second |

The arithmetic agrees: `44,100 × 4 = 7,350 × 24 = 75 × 2,352 = 176,400 bytes/s`.

The physical channel includes error correction, interleaving, control information, synchronisation and **eight-to-fourteen modulation**, EFM. The coding chain combines 24 audio-data bytes with eight parity bytes and one control byte into 33 symbols, with interleaving across frames. Each symbol occupies 14 channel bits. Ordinary symbols use the EFM mapping table; the first two control-symbol positions in each 98-frame section instead carry special 14-bit synchronisation patterns, SYNC 0 and SYNC 1. Including three merging bits per symbol and 27 synchronisation/merging bits gives `33 × (14 + 3) + 27 = 588` channel bits per frame. At 7,350 frames per second, the physical channel rate is 4,321,800 channel bits per second. This exceeds the 1,411,200 bit/s audio payload because the two rates count different things. Interleaving also means that logical audio blocks should not be drawn as unchanged neighbouring samples directly under the laser. [Ecma International, ECMA-130, shared CD physical coding, especially §§17–21](https://ecma-international.org/wp-content/uploads/ECMA-130_2nd_edition_june_1996.pdf).

A pressed disc has a spiral track with pits and lands. An optical pickup detects the changing reflected signal. Electronics recover timing and channel data, undo the modulation and interleaving, and correct recoverable errors. The decoder then supplies PCM for playback. A pit is **not one PCM bit**. In the channel representation, transitions and constrained run lengths carry coded information.

Error correction recovers original data when the damage is within the system’s capability. Concealment estimates or substitutes for data that cannot be recovered; it is a different operation. A readable-looking disc and a successful playback do not by themselves prove that every extracted sample is correct.

These mechanisms were a central part of making consumer digital audio practical. Sony’s account describes the development of optical playback and error correction: [Digitizing Music](https://www.sony.com/en/SonyInfo/CorporateInfo/History/SonyHistory/2-07.html).

### From early digital recording to current distribution

Digital recording existed before consumer audio CDs. Denon’s documented 1972 DN-023R system is one early commercial PCM example. Such a recording could still reach listeners on an analogue LP: the recording method and the distribution medium are separate facts. [Denon, Legacy of Firsts](https://www.denon.com/en/inside-denon/brand-stories/legacy-of-firsts.html).

| Period or milestone | What changed | What to distinguish |
| --- | --- | --- |
| Digital recording before the CD | PCM could be recorded through specialised equipment, including systems based on video-recording technology | A digitally recorded performance need not have a digital consumer release |
| 1982 commercial CD introduction in Japan | Consumers could buy a standard digital audio disc and player | The commercial launch followed years of development and earlier PCM work |
| Late 1980s DAT | Digital Audio Tape made PCM recording available on a small magnetic-tape format | Tape is a physical medium; digital describes the encoded information |
| Recordable optical discs | A compatible recorder could write digital audio or computer data to recordable media | An audio CD-R and a data CD-R can contain different logical formats |
| 1992 MiniDisc | Sony introduced a smaller recording and playback system using ATRAC audio compression | The original music format used lossy coding; “digital disc” does not imply uncompressed PCM |
| 1990s MP3 and AAC | Perceptual coding reduced distribution and storage requirements | MPEG-1 Audio Layer III and AAC are different coding systems |
| 1999 SACD and the DVD-Audio era | Optical releases offered alternative high-resolution and multichannel systems | SACD’s DSD representation differs from DVD-Audio’s PCM-based approach |
| File-based recording and editing | Audio became directly accessible as files on disk and solid-state storage | The file, its codec, its metadata and its physical storage device are separate layers |
| Network streaming and wireless playback | Encoded audio could arrive in packets or segments, with buffering and negotiated playback paths | “Streaming”, “Bluetooth” and “lossless” describe different aspects of delivery |

Sony documents the 1982 Japanese CD launch, its 1987 DAT product and the 1992 MiniDisc launch in its historical material. The MPEG-1 standard was finalised in 1992; the familiar `.mp3` filename extension was selected in 1995. Those dates describe different milestones. [Sony product history](https://www.sony.com/en/SonyInfo/CorporateInfo/History/sonyhistory-e.html); [Sony DAT history](https://www.sony.com.mx/corporate/MX/acerca/infocorporativa/historia_productos_homeaudio.html); [Sony, Digitizing Music](https://www.sony.com/en/SonyInfo/CorporateInfo/History/SonyHistory/2-07.html); [Fraunhofer, MP3 and AAC Explained](https://www.iis.fraunhofer.de/content/dam/iis/de/doc/ame/conference/AES-17-Conference_mp3-and-AAC-explained_AES17.pdf); [Fraunhofer, 30 Years of .mp3](https://www.iis.fraunhofer.de/en/magazin/panorama/2025/30-years-of-mp3.html).

SACD was launched in 1999 using **Direct Stream Digital**, DSD. Its original 2.8224 MHz, one-bit representation uses a high-rate, noise-shaped bitstream. It should not be compared with multibit PCM by looking at “one bit” alone: the representation, rate and filtering differ. DVD-Audio supported PCM-based high-resolution and multichannel configurations, including Meridian Lossless Packing, MLP. Neither label guarantees a superior original recording or master. [Sony’s SACD announcement](https://www.sony.com/en/SonyInfo/News/Press/199904/99-042/); [IASA guidance on DVD-Audio](https://www.iasa-web.org/tc04/issues-dvd-audio-dvd); [Meridian 568 handbook, MLP](https://www.meridian-audio.com/download/Handbooks/500_Series/568user.pdf).

There is no single final replacement for all these systems. Production, preservation, physical distribution, low-latency communication and consumer listening impose different requirements.

### Two meanings of compression

**Data compression** reduces the number of bits needed to represent information. **Dynamic-range compression** changes the level relationship between quieter and louder passages.

A compressor plug-in may reduce the gain applied above a threshold. Its output can be stored as uncompressed PCM. Conversely, a losslessly compressed FLAC file can contain audio with an unchanged dynamic range. “The track is compressed” is therefore ambiguous unless the context identifies the process.

**Lossless audio compression** permits exact recovery of the sample values supplied to that encoder. **Lossy audio compression** permits a smaller representation by allowing irreversible changes to those values. Losslessness is a relationship between an encoder’s input and its decoder’s output. It does not mean an ADC captured an infinitely precise acoustic event or that an earlier lossy stage never existed.

![Lossless predictive coding stores exact residual information; a representative lossy perceptual codec quantises transformed data. Containers are separate packaging and dynamic range compression is a different operation.](https://damjan-popic.github.io/assets/images/agrft/v2/audio-compression.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/audio-compression.svg)

### Lossless coding: store a prediction and an exact correction

Audio often has relationships between neighbouring samples. A lossless encoder can exploit those relationships instead of writing every value independently at the same word length.

Consider this original eight-sample example:

`1000, 1002, 1003, 1003, 1000, 998, 999, 1001`

Choose the previous sample as the prediction for the next. Store the first value, then the prediction errors, called **residuals**:

`first value: 1000; residuals: +2, +1, 0, −3, −2, +1, +2`

The decoder starts at 1,000 and adds each residual to the previously reconstructed value. It recovers all eight original integers exactly.

A toy representation can store the first value in 16 bits and each residual in four signed bits. That uses `16 + 7 × 4 = 44` payload bits instead of `8 × 16 = 128`, before headers and padding. This particular four-bit scheme would fail for a residual outside −8 to +7 unless it supplied another representation. A real codec must handle every permitted input, including difficult or noisy passages.

FLAC uses blocks, prediction choices and residual coding; it can also select representations appropriate for constant or poorly predictable material. Entropy coding gives frequent small patterns shorter representations. Its defined decoding process reconstructs the original integer samples. [IETF, RFC 9639](https://www.rfc-editor.org/rfc/rfc9639.html).

Compression ratio depends on the material and settings. A “higher compression” lossless setting can spend more work finding an efficient representation while preserving the same decoded samples. It is not a higher sound-quality setting.

A lossless round trip also need not recreate the entire original file byte for byte. Container headers, chunk order and metadata can differ even when the decoded audio samples are identical. When verifying preservation, distinguish an audio-data comparison from a whole-file checksum comparison.

### Lossy coding: control the error people may hear

A perceptual encoder models which errors are likely to be less audible in a particular signal. A strong component can mask weaker nearby components; the time relationship also matters. Masking is a conditional property of hearing, not permission to remove every quiet sound.

A typical transform-based encoding chain has several stages:

1. Divide audio into overlapping analysis blocks.
2. Transform or filter the block into a frequency-related representation.
3. Analyse the signal and estimate perceptual requirements.
4. Allocate a limited number of bits and quantise the representation.
5. Encode the quantised values and the information required to decode them.
6. Package the resulting stream for storage or transmission.

The transform alone need not be the irreversible step. Loss often enters through quantisation and other approximations made to meet the bit budget. Entropy coding afterwards can be reversible even though the complete codec is lossy. MP3 and AAC use different tools and bitstream structures within the broad perceptual-coding approach. [Fraunhofer, MP3 and AAC Explained](https://www.iis.fraunhofer.de/content/dam/iis/de/doc/ame/conference/AES-17-Conference_mp3-and-AAC-explained_AES17.pdf); [Fraunhofer’s EVS technical overview, comparison of speech and perceptual coding](https://www.iis.fraunhofer.de/content/dam/iis/de/doc/ame/wp/FraunhoferIIS_Technical-Paper_EVS.pdf).

A numerical model makes irreversibility visible. Suppose a transform coefficient of 9.7 is rounded to 10 using a one-unit step. Several original values could have produced 10. The decoder cannot know which one occurred. It reconstructs according to the encoded value and scale. Increasing the available precision can reduce that error, but requires more bits.

At a constrained bit rate, difficult material may expose artefacts such as pre-echo around a transient, warbling textures or altered high-frequency detail. The results depend on the codec, encoder, settings and source. Listening comparisons should use matched levels and the same source segment. A spectrogram can support analysis, but an empty frequency region alone does not quantify overall perceived quality.

**Constant bit rate**, CBR, aims at a specified data rate. **Variable bit rate**, VBR, changes the allocation as the material changes. **Average bit rate**, ABR, targets an average across a duration. Exact behaviours and available modes are codec-dependent.

Stereo coding may exploit similarities between channels. This does not necessarily mean deleting one channel. Mathematically reversible combinations such as sum and difference can remove redundancy; other modes can make perceptual approximations. The selected coding mode matters. [Xiph.Org, Vorbis channel coupling](https://xiph.org/vorbis/doc/stereo.html).

### Codecs, containers and filenames

A **codec** specifies how audio is encoded and decoded. A **container** organises streams and associated information. A **file extension** is a naming convention. These categories overlap in everyday speech, so describe the actual contents when precision matters.

| Name | Type and typical role | Essential distinction |
| --- | --- | --- |
| Linear PCM / LPCM | Uncompressed sample representation | Needs sample format, rate, channels and packing specified |
| WAVE / WAV | RIFF-based audio container | Often PCM, but a `.wav` extension alone does not prove PCM or a particular bit depth |
| BWF | Broadcast Wave conventions and metadata | Supports production identification and timing information; it is not a lossy codec |
| RF64 / BW64 | Larger WAVE-related file structures | Address large files and metadata requirements; check receiving-software support |
| AIFF / AIFF-C | Audio file formats | Classical AIFF commonly carries uncompressed PCM; the related AIFF-C permits other encodings |
| CAF | Apple Core Audio Format container | Can carry different audio encodings; the container name does not identify one codec |
| FLAC | Lossless integer-audio codec and native stream format | The decoded sample values match the encoder input |
| ALAC | Apple Lossless Audio Codec | Commonly carried in an MPEG-4 audio file; `.m4a` does not necessarily mean AAC |
| MP3 | MPEG-1/2 Audio Layer III | Lossy audio coding; it is not MPEG-3 video |
| AAC family | Advanced Audio Coding and related extensions/profiles | Lossy coding; profile and configuration matter |
| Vorbis | Perceptual audio codec | Often in Ogg; Ogg is a container |
| Opus | Lossy speech and music codec | Used for interactive and stored audio; transport and container can vary |
| Dolby Digital / AC-3 | Lossy multichannel audio coding | A codec, distinct from a speaker layout |
| Dolby Digital Plus / E-AC-3 | Lossy audio coding used in delivery | Can carry Dolby Atmos information in supported configurations |
| Dolby TrueHD | Lossless audio coding | Different from Dolby Digital Plus despite the shared brand |
| DSD | High-rate, noise-shaped one-bit representation | Distinct from conventional multibit PCM |
| MIDI | Musical event and control data | A note instruction does not contain the recorded sound of the instrument |

Apple’s [Core Audio Essentials](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/CoreAudioEssentials/CoreAudioEssentials.html), the [ALAC project](https://github.com/macosforge/alac/blob/master/ReadMe.txt), the [Vorbis specification](https://xiph.org/vorbis/doc/Vorbis_I_spec.html), [RFC 6716 on Opus](https://www.rfc-editor.org/rfc/rfc6716.html), the [MIDI Association’s overview](https://midi.org/about-midi-part-1overview), and Dolby’s descriptions of [Digital Plus](https://professional.dolby.com/technologies/dolby-digital-plus/) and [TrueHD](https://professional.dolby.com/tv/dolby-truehd) document these distinctions.

BWF can store a time reference expressed as a sample count. That aids placement but does not guarantee that a device ran at the correct rate. RF64 is widely encountered in recorder workflows; the EBU subsequently directed its formal large-file standardisation to ITU-R’s BW64 recommendation. The “64-bit” here concerns file structures and sizes, not a demand for 64-bit audio samples. [EBU Tech 3285](https://tech.ebu.ch/docs/tech/tech3285.pdf); [EBU Tech 3306](https://tech.ebu.ch/docs/tech/tech3306.pdf); [ITU-R BS.2088](https://www.itu.int/rec/R-REC-BS.2088/en).

### Channels, objects and contemporary delivery

A mono file contains one channel. A stereo file contains two. Two recorded microphone channels do not automatically form a coherent stereo recording: they may be unrelated isolated tracks.

A channel-based surround mix assigns signals to defined playback channels. The `.1` in 5.1 denotes a low-frequency-effects channel, not one tenth of a full-bandwidth sample or one tenth of the file. Channel order must be identified; six unnamed channels are an incomplete delivery description.

Object-based audio combines audio with information about its intended presentation, allowing a renderer to adapt it to supported playback arrangements. **Dolby Atmos** identifies an immersive audio system; the name alone does not establish whether a delivered stream uses lossless or lossy coding. Metadata is part of how the system is interpreted. [Dolby, Atmos for sound bar applications](https://professional.dolby.com/siteassets/tv/home/dolby-atmos/dolby-atmos-for-sound-bar-applications.pdf).

Streaming changes how audio reaches the listener. A player can request successive segments, buffer them and decode them while playback continues. Different representations may serve different bandwidth conditions. The delivery system still needs a codec, timing information and a playback path. [IETF, RFC 8216, HTTP Live Streaming](https://www.rfc-editor.org/rfc/rfc8216.html).

Wireless headphones may introduce another codec stage after the player decodes the source. Bluetooth LE Audio uses the LC3 codec within its defined architecture; supported behaviour depends on both endpoints. Consequently, “the source file is lossless” does not describe every later link to the listener. Avoid inferring an end-to-end path from a single logo. [Bluetooth SIG, LE Audio specifications](https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/le-audio-specifications/).

### Sample rate, playback speed and synchronisation

Changing a sample-rate label is different from sample-rate conversion. Suppose 44,100 samples were recorded during one second. If software plays those same samples at 48,000 samples per second without resampling, they last:

`44,100 / 48,000 = 0.91875 seconds`

Playback is about 8.84% faster, and the frequencies rise by the factor `48,000/44,100 ≈ 1.08844`. Correct sample-rate conversion reconstructs and filters an appropriate representation, then generates a new sample sequence at the destination rate while preserving the intended duration and pitch.

Independent recorders can also drift when both display “48 kHz”. Their clocks are physical oscillators with finite accuracy. A relative rate error of 50 parts per million accumulates approximately:

`50 / 1,000,000 × 3,600 s = 0.18 seconds per hour`

At 25 video frames per second, that is 4.5 frames. This is a stated example, not the specification of every recorder.

**Timecode** labels positions. **Word clock** governs audio sample timing. **Genlock** concerns video timing. A timecode jam can align labels while devices subsequently run on independent clocks. Whether a device derives its sample timing from a received reference depends on its design and settings. Sound Devices’ [synchronisation guidance](https://support.sounddevices.com/hc/en-us/articles/44141193080987-Syncing-the-788T-with-External-Video-and-Audio) explicitly distinguishes the relevant clocks.

In dual-system production, camera and sound recorder create separate recordings. A slate gives a visual and audible reference event; timecode can support automatic matching; compatible clock arrangements reduce drift. Check the beginning and the end of a long take. Correct alignment at one instant does not prove matching speed throughout.

At 48 kHz and exactly 25 fps, one video-frame duration contains `48,000/25 = 1,920` audio sample frames. At a fractional frame rate, the relationship need not be an integer for each individual frame. Do not “fix” sound by dropping arbitrary samples until a waveform seems to line up.

### Choose and describe a production file

For a worked production example, specify: **48 kHz, 24-bit integer PCM in BWF, four labelled mono tracks, with an agreed timecode frame rate and take metadata**. This is an explicit classroom specification, not a universal requirement.

The boom and radio microphones can remain on isolated tracks. A production mix is a separate routing decision. Keeping isolated sources allows later editing choices; it does not replace monitoring or good microphone placement.

Keep original recordings intact. Use working copies for processing and a documented master for export. If the destination requests AAC, generate that delivery from the suitable master. Re-encoding MP3 as AAC applies another lossy stage; exporting the MP3 as WAVE only stores its decoded approximation in a larger representation. FLAC can preserve that approximation exactly, but cannot restore the original pre-MP3 samples.

An effective technical description names the stage, operation and consequence:

- “The ADC outputs 48,000 samples per second for each channel.”
- “The 24-bit word length gives more amplitude codes; it does not increase the sample rate.”
- “The container stores the stream and its metadata.”
- “This lossless decoder reconstructs the original sample values supplied to the encoder.”
- “The audio is aligned at the slate but drifts later, so we need to investigate the recording rates.”
- “The file is floating point, but the microphone electronics may still have overloaded.”

### Working vocabulary

The Slovene expressions provide orientation; some departments routinely use the English term.

| English | Slovene orientation | Precise use |
| --- | --- | --- |
| sound pressure | zvočni tlak | Acoustic pressure variation |
| waveform | valovna oblika | Signal value plotted against time |
| frequency | frekvenca | Cycles per second |
| amplitude | amplituda | Magnitude of variation, with a stated convention |
| phase | faza | Position within a cycle relative to a reference |
| polarity | polarnost | Sign or electrical orientation |
| transducer | pretvornik | Device converting between physical forms of energy |
| diaphragm | membrana | Moving element in a microphone or loudspeaker |
| preamplifier | predojačevalnik | Stage amplifying a small input signal |
| gain | ojačenje | Multiplicative change in signal level |
| sample | vzorec | One value for one channel at a sample instant |
| sample frame | skupina sočasnih vzorcev kanalov | One sample from each channel at an instant |
| sample rate | frekvenca vzorčenja | Sample instants per second per channel |
| bit depth / word length | bitna globina / dolžina besede | Size and representation of a sample word |
| quantisation | kvantizacija | Assignment to representable values |
| aliasing | prekrivanje spektralnih komponent pri vzorčenju | Ambiguity caused by indistinguishable sampled frequencies |
| anti-alias filter | filter proti prekrivanju spektrov | Restricts input bandwidth before sampling |
| reconstruction filter | rekonstrukcijski filter | Suppresses unwanted images after conversion |
| noise floor | raven šuma | Background noise level under stated conditions |
| headroom | rezerva do mejne ravni | Margin before a specified limit |
| clipping | rezanje vrhov / prekrmiljenje | Limiting that destroys the original peak shape |
| dither | dither / namerno dodani šum | Noise used to control quantisation error |
| residual | preostanek / napaka napovedi | Difference between a sample and its prediction |
| lossless | brezizguben | Exact recovery of the specified encoder input |
| lossy | izguben | Irreversible approximation allowed |
| bit rate | bitna hitrost | Bits per second |
| codec | kodek | Encoding and decoding system |
| container | vsebnik | File or stream organisation |
| buffer | medpomnilnik | Temporarily holds data awaiting processing or playback |
| latency | zakasnitev | Delay through a system |
| clock drift | lezenje časovne osnove | Accumulating timing difference |
| isolated track / ISO | ločena posneta sled | Independently recorded source or feed |
| stem | podmiks sorodnih elementov | For example, dialogue, music or effects submix |
| master | osnovni končni zapis | Agreed source for subsequent deliverables |

## 3. How digital video works

A video file contains instructions and numerical data from which a player can reconstruct changing pictures, sound and their timing. The file does not contain miniature moving photographs. Its images may be stored as independently coded pictures, or a decoder may have to reconstruct one picture using others. Understanding video therefore means following several connected processes: measuring an image, representing its samples, compressing them, organising the results, and displaying them at the intended times.

This chapter begins with analogue television because many digital conventions preserve decisions made for scanning, transmission and compatibility. It then follows a picture into a digital file. The camera chapter explains how light first becomes an electrical signal.

### The questions hidden inside “What format is it?”

A useful technical description answers several different questions.

| Property | What it tells us | Example |
| --- | --- | --- |
| Image dimensions | The number of stored sample positions across and down the picture | 1920 × 1080 |
| Frame rate and scan | How pictures or fields are ordered in time | 25 progressive frames per second |
| Sample representation | Which numerical components describe the image | Y′CbCr, 10 bits per component, 4:2:2 |
| Colour interpretation | How numbers relate to colours and light levels | Specified primaries, transfer function, matrix and range |
| Video codec | How image information is encoded and reconstructed | H.264/AVC, HEVC, ProRes, FFV1 |
| Container | How video, audio, timing and metadata are organised | MP4, MOV, MXF or Matroska |

A seventh question is **purpose**: is this a camera original, an editing proxy, a preservation master, a graded master or a viewing copy? Two files can have the same extension and serve very different purposes. “A four-kay em-pee-four” is insufficient for a technical handover.

**Model explanation:** “The file is a 1920-by-1080 progressive recording at twenty-five frames per second. The video is ten-bit 4:2:2. I still need to check the codec, colour metadata and audio layout before preparing the export.”

The separation of colour-identification fields from compression is formalised in [ITU-T H.273](https://www.itu.int/rec/T-REC-H.273). Containers such as [Matroska, specified in RFC 9559](https://www.rfc-editor.org/rfc/rfc9559.html), organise several kinds of media and metadata.

### Analogue video: a changing voltage with a timetable

An analogue picture signal varies continuously in amplitude within the bandwidth of the system. In a traditional television raster, a scanning process represents successive positions along a line, then successive lines down the picture. A corresponding display uses timing information to put the signal back in the right place. **Raster** means this organised arrangement of scanning lines.

Imagine a monochrome camera looking at a white card with a black vertical stripe. During the active part of a line crossing the stripe, the picture signal goes from a high level to a low level and back. The time at which the level changes identifies the stripe’s horizontal position. Its duration identifies the stripe’s width. A darker stripe is represented by a different amplitude, not by a binary word.

This example separates three ideas. The line has a time structure; its amplitude carries picture information; its permitted rate of change is limited by bandwidth. Very narrow alternating stripes require rapid signal changes. When the system cannot carry those changes, the stripes lose contrast or merge. “Analogue has no pixels” consequently does not mean “analogue has unlimited detail”. Traditional television already has a finite number of scan lines and finite temporal and electrical bandwidths.

A magnetic videotape does not ordinarily record this baseband waveform as a literal line of unmodified voltage. Its recording system modulates and arranges signals so that magnetic heads and tape can carry them. The playback electronics recover a usable video signal. **Carrier**, **recording format** and **output signal** describe different stages.

Technical references: [Analog Devices, “Understanding Analog Video Signals”](https://www.analog.com/en/resources/technical-articles/understanding-analog-video-signals.html); [IASA-TC 06, Part C: video carriers and signal extraction](https://www.iasa-web.org/sites/default/files/publications/IASA-TC_06-C_v2019.pdf).

### What is inside one analogue television line?

![Functional PAL composite line waveform with sync tip minus point three volts, zero blanking reference, nominal white point seven volts, back porch burst and active luma, with 64 microsecond period and approximate 4.7 microsecond sync duration. Horizontal intervals not to scale.](https://damjan-popic.github.io/assets/images/agrft/v2/video-analogue-line.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/video-analogue-line.svg)

The figure represents a normal picture line in a conventional 625-line PAL system. It is a functional waveform diagram, not an alignment test signal. Vertical synchronisation intervals have a different pulse structure.

| Part of the line | Function |
| --- | --- |
| Active video | Carries the visible picture information for that line |
| Front porch | A brief blanking interval after active video and before the next line-sync pulse |
| Horizontal sync pulse | Provides a timing reference for the next line |
| Back porch | The blanking interval after line sync and before active video |
| Colour burst | A short reference oscillation used by the PAL/NTSC colour decoder |
| Blanking interval | The interval allocated to timing and associated non-picture functions |

Following a line from its sync pulse, the order is **sync, back porch with burst, active video, front porch, next sync**. Following it from active video gives the same cycle with a different starting point. The waveform must not label the burst as part of the visible picture.

For a conventional 625/50 system, 625 lines per frame multiplied by 25 frames per second gives **15,625 lines per second**. One complete line therefore lasts **64 microseconds**. A normal line-sync pulse is approximately **4.7 microseconds**. These figures describe that system, not every signal called PAL. In a normal PAL waveform with blanking taken as zero, nominal black is at blanking level, nominal white is about +0.7 V and sync tip about −0.3 V; the signal is specified with its intended termination.

The amplitude of a composite colour signal includes chrominance as well as luma. Its instantaneous excursions are therefore not simply a direct brightness trace. Do not read every peak in composite video as a white object.

Reference: the conventional systems and their different timing parameters are tabulated in the historical [ITU-R BT.470-6](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.470-6-199811-S!!PDF-E.pdf). See also [Tektronix, standard and HD video measurements](https://www.tek.com/en/documents/primer/guide-standard-hd-digital-video-measurements).

### Composite, S-Video and component connections

**Composite video**, also called **CVBS**, combines picture components and synchronisation into one video signal. In PAL and NTSC, colour information modulates a colour subcarrier. A receiver must separate the colour information from luma. Imperfect separation can produce moving dots at colour boundaries or false colour on fine monochrome detail.

**S-Video**, or **Y/C**, carries luma with synchronisation separately from the modulated chrominance signal. It avoids combining those two channels at that connection. It does not undo losses already present in a tape or an earlier composite recording.

**Component video** keeps picture components separate. Common analogue arrangements include RGB and Y′PbPr. In Y′PbPr, Y′ carries luma and Pb and Pr are scaled colour-difference signals. Connector colours help identify connections but do not define the signal by themselves. A BNC connector, for example, can carry analogue video, digital SDI or other signals.

The term **YUV** is often used loosely in software for digital luma/chroma formats. When explaining a specified digital recording, **Y′CbCr** is normally the more precise designation. Analogue U and V and digital Cb and Cr are related concepts with different definitions and scaling. They should not be substituted blindly in an equation.

Reference: [Analog Devices, “Video Basics”](https://www.analog.com/en/resources/technical-articles/basics-of-analog-video.html).

**Useful English:** “The deck provides a composite output and a separate Y/C output. We should identify the signal path before choosing the capture settings.” Say **output**, **input**, **connect**, **terminate**, **decode**, **separate** and **recover** when describing this process.

### PAL, NTSC, VHS and the problem of names

PAL and NTSC identify colour-television encoding systems associated with particular television-system families. They are not universal synonyms for 720 × 576 and 720 × 480, and they are not video codecs inside an ordinary modern MP4.

The familiar European association is **625 lines, 50 fields per second**, while the familiar colour NTSC association is **525 lines, 60/1.001 fields per second**. Variants exist: the letters alone do not supply every timing parameter. The total line counts include intervals outside the active picture.

**VHS** identifies a videotape recording format. PAL-system VHS and NTSC-system VHS recordings require suitable playback equipment; a VHS cassette’s shape does not tell a capture device how to interpret its contents. **S-VHS** is a recording format, whereas **S-Video** names a separated video connection. Similar names do not make them interchangeable.

A **LaserDisc** is an optical carrier whose conventional video is analogue. The presence of a laser does not make the picture digital. A DVD-Video, by contrast, contains digital coded material and navigation structures. A **MiniDV** cassette contains a digital recording. Tape is therefore not inherently analogue, and an optical disc is not inherently digital.

References: [Library of Congress, videorecording formats](https://loc.gov/marc/bibliographic/bd007v.html); [Library of Congress, DV encoding](https://www.loc.gov/preservation/digital/formats/fdd/fdd000183.shtml); [IASA-TC 06](https://www.iasa-web.org/tc06/guidelines-preservation-video-recordings).

### Fields, frames and progressive scanning

![Illustrative alternating-line capture of a moving vertical object in two fields separated by twenty milliseconds, followed by a woven combination showing combing; explains fifty fields and twenty-five field pairs per second.](https://damjan-popic.github.io/assets/images/agrft/v2/video-fields.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/video-fields.svg)

A **progressive frame** represents a complete raster in one frame interval. An **interlaced frame** consists of two fields containing alternating lines. In genuinely interlaced acquisition, the fields represent different moments. One field contains one set of line positions, and the following field contains the complementary set.

In a 50-field-per-second system, successive fields are separated by **20 ms**. A field pair spans a **40 ms** frame interval, giving **25 interlaced frames per second**. A moving hand changes position between the fields. If software weaves both fields into one still picture, the hand can acquire comb-like edges. The effect reveals a temporal mismatch between alternating lines.

The compact label **1080i50** is commonly used for 1080-line interlaced video with 50 fields per second. In formal frame-oriented notation the same basic temporal arrangement may be described as **1080i/25**. Specifications use different conventions, so write out “50 fields per second, 25 interlaced frames per second” when ambiguity matters. **1080p50** instead has 50 complete progressive frames per second.

**Field order** identifies which field is temporally first. “Upper first” and “lower first” refer to that ordering. Reversing it can make motion appear to step backwards and forwards. Field order is a property to inspect, not something to guess from the word “interlaced”.

A frame and a photograph are not identical concepts. Even a progressive camera may read different rows at slightly different times. That sensor behaviour is explained under rolling shutter in the camera chapter. Here, progressive describes the video picture organisation.

References: [Apple, field order](https://help.apple.com/motion/mac/5.0/help/English/en/motion/usermanual/chapter_B_section_3.html); [Apple, overriding field metadata](https://support.apple.com/en-qa/guide/final-cut-pro/verb90b3038f/mac).

### Deinterlacing, segmented frames and film cadence

**Deinterlacing** constructs progressive output from interlaced input. Simply discarding one field throws away its line samples and, for genuinely interlaced motion, half the temporal observations. Simply weaving fields preserves their samples but combines different moments.

A motion-adaptive method can combine fields in static areas and estimate missing lines differently in moving areas. A field-rate output can produce 50 progressive output pictures per second from 50-field input. This preserves the original sequence of motion observations more closely than making 25 progressive pictures, although each output still requires reconstruction of unrecorded line positions.

The correct operation also depends on the source. **Progressive segmented frame**, or **PsF**, transports the two segments of a progressive picture in an interlace-like arrangement. They do not represent two separate acquisition moments. Material transferred from film may contain repeated fields following a cadence. **Inverse telecine** attempts to recover the underlying progressive frames from a recognised transfer pattern. A deinterlacer applied without understanding the source can soften or disturb material unnecessarily.

For preservation, keep the original captured field structure and documented interpretation in the master. Make a separately identified deinterlaced viewing derivative when required. The viewing file and the capture master perform different jobs.

References: [vMix, progressive segmented frames](https://video.vmix.com/knowledgebase/article.aspx/142/what-does-psf-mean); [FFmpeg, bwdif and field-based deinterlacing](https://ffmpeg.org/ffmpeg-filters.html#bwdif); [Library of Congress, video streams as sources](https://loc.gov/preservation/digital/formats/content/video_source.shtml); [IASA-TC 06, Part B](https://www.iasa-web.org/sites/default/files/publications/IASA-TC_06-B_v2019.pdf).

### How an analogue tape becomes a digital file

A conventional capture chain contains identifiable operations:

1. **Playback:** the correct deck transports the tape and recovers its recorded signals.
2. **Signal conditioning and timing correction:** the chain establishes usable levels and stable timing.
3. **Colour decoding and sampling:** a decoder separates the components; analogue-to-digital conversion represents measured amplitudes numerically.
4. **Capture and file creation:** the computer receives the digital stream and stores picture, sound, timing and metadata.
5. **Verification:** the operator checks the file, the signal and the correspondence with the source.

The implementation may combine several operations in one device, and a decoder may digitise composite video first and separate its components digitally. The diagram is a functional sequence, not a claim that every box requires a separate appliance.

A **time-base corrector**, or **TBC**, addresses timing instability associated with playback. A moving tape and rotating heads do not reproduce every line at perfectly uniform intervals. Timing errors can appear as horizontal displacement or an unstable picture. Time-base correction stabilises timing; it does not recover detail that the recording never contained. Different line and frame correction devices also have different capabilities.

Capture settings must describe the source and the chosen representation: field order, sample dimensions, aspect ratio, component precision, chroma sampling, audio configuration and range. A 4K capture file cannot manufacture four-kay detail from a VHS recording. It can merely store an enlarged or reprocessed representation.

A digital tape transfer may allow the existing recorded bitstream to be transferred directly. Sending such a tape through an analogue output and re-digitising it introduces an avoidable conversion if a suitable direct transfer is possible.

References: [IASA-TC 06, Part D: planning and workflows](https://www.iasa-web.org/sites/default/files/publications/IASA-TC_06-D_v2019.pdf); [Library of Congress, DV encoding and transfer](https://www.loc.gov/preservation/digital/formats/fdd/fdd000183.shtml).

### Sampling a line: the bridge to digital television

Sampling measures a signal at selected times; quantisation assigns each measurement a numerical value. As in audio, an anti-aliasing filter limits the signal before sampling. In video, the samples must also have a known relationship to lines and fields.

The 13.5 MHz luma sampling family in **BT.601** is a useful concrete example. Luma is sampled **13.5 million times per second**; each colour-difference channel in 4:2:2 is sampled at **6.75 MHz**. For a 625-line system:

`13,500,000 samples/s ÷ 15,625 lines/s = 864 luma samples per complete line`

The digital active line contains **720 luma samples**, with **360 samples in each chroma channel**. The complete sampled line and the active picture width are different quantities. For the corresponding 525-line system there are **858 luma samples per complete line**, while the active width is again 720.

Do not confuse the width of the standard digital active window with the precise active interval of every analogue source. They are related through defined timing, and the actual image may include edge blanking or other non-picture material.

Reference: [ITU-R BT.601-7, Annex 1, Table 3](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.601-7-201103-I!!PDF-E.pdf).

### Pixels are samples with an interpretation

A stored picture is an ordered array of samples. A pixel position might have three RGB component values, but a subsampled representation does not store three independent values at every position. The image still has a full luma grid; colour components can have smaller grids.

A display pixel is a physical light-producing or light-modulating element. A stored pixel is a data location in an image representation. Scaling, colour conversion and display reconstruction stand between them. One stored pixel does not necessarily map onto one display pixel, and a pixel’s numerical value is not itself a quantity of light until the relevant interpretation is known.

For an uncompressed, full-range RGB example, take one pixel with eight bits in each component:

| Component | Decimal code | Eight-bit binary word |
| --- | --- | --- |
| R′ | 128 | `10000000` |
| G′ | 64 | `01000000` |
| B′ | 32 | `00100000` |

The three words require **24 bits**, or **3 bytes**, before any padding, alpha channel or file structure. In a stated RGB byte order they would be written as `80 40 20` in hexadecimal. A different memory layout could order components differently. These bytes also need colour information: “128 red” does not specify the same physical colour across every colour space and transfer function.

With unsigned integer coding, eight bits provide **256 possible codes**, ten bits **1024**, and twelve bits **4096**. The largest code is one less than the number of codes because counting starts at zero. Three independently represented eight-bit components permit 256³ = **16,777,216** numerical combinations. This is not a promise that a camera can distinguish that many perceptually different colours in every scene.

For examples of the distinction between component precision and memory layout, see [Microsoft, 10-bit and 16-bit video formats](https://learn.microsoft.com/en-us/windows/win32/medfound/10-bit-and-16-bit-yuv-video-formats).

### Width, height and aspect ratio

A 1920 × 1080 image has **2,073,600 sample positions**. A 3840 × 2160 UHD image has **8,294,400**, four times as many. Doubling both dimensions quadruples the number of positions; it does not merely double them.

**Storage aspect ratio** describes the ratio of stored width to height. **Pixel aspect ratio**, also called **sample aspect ratio**, describes the intended width-to-height proportion of a sample in display geometry. **Display aspect ratio** describes the intended picture shape. For the same uncropped image:

`display aspect ratio = (stored width ÷ stored height) × pixel aspect ratio`

With square pixels, 1920/1080 = 16/9. For a deliberately simplified example, displaying the entire 720 × 576 array as 4:3 requires a pixel aspect ratio of 16:15. Displaying that entire array as 16:9 requires 64:45. Historical SD standards and applications may distinguish a clean aperture or 702/704-sample picture region from the complete stored width. Inspect the intended aperture and metadata before assigning a ratio mechanically.

**UHD 3840 × 2160** and the **4096 × 2160 digital-cinema container** are different dimensions. “4K” alone is ambiguous. A cinema image can also occupy a specified flat or scope region within the container.

References: [ITU-R BT.2020](https://www.itu.int/rec/r-rec-bt.2020/en); [DCI, Digital Cinema System Specification](https://www.dcimovies.com/dci-specification/); [Matroska’s separate pixel and display dimensions](https://www.rfc-editor.org/rfc/rfc9559.html).

### From RGB to luma and colour difference

In a linear-light RGB representation, the component values are proportional to the corresponding light contributions. Many video representations first apply a non-linear transfer function. A prime mark, as in **R′G′B′**, indicates the non-linear quantities.

**Luminance** is a light-related quantity with a defined colorimetric meaning. **Luma**, Y′, is a weighted combination of non-linear video components. They are related, but they are not interchangeable terms. Calling luma “brightness” can orient a beginner, provided the more precise distinction follows.

For the non-constant-luminance BT.709 representation, using normalised components:

`Y′ = 0.2126R′ + 0.7152G′ + 0.0722B′`

`Cb = (B′ − Y′) ÷ 1.8556`

`Cr = (R′ − Y′) ÷ 1.5748`

These normalised colour differences must then be scaled and offset into the chosen digital code range. They are not yet the unsigned Cb and Cr code words stored in a file.

For a red input R′ = 1, G′ = 0, B′ = 0, the arithmetic gives Y′ = 0.2126, Cb ≈ −0.1146 and Cr = 0.5. Using eight-bit narrow-range scaling and rounding gives approximately **Y′ 63, Cb 102, Cr 240**. The corresponding blue input has a much lower luma value because the blue coefficient is smaller.

The decoder uses all three components to reconstruct RGB. Luma alone cannot identify the original colour. The coefficients also matter: the BT.601 luma weighting differs from BT.709. Interpreting one matrix as the other changes colours without changing the file’s nominal dimensions.

Reference: [ITU-R BT.709-6, signal construction and digital representation](https://www.itu.int/dms_pubrec/itu-r/rec/bt/r-rec-bt.709-6-201506-i!!pdf-e.pdf).

### Chroma subsampling: what 4:4:4, 4:2:2 and 4:2:0 retain

![Separate luma Cb and Cr grids over a two-by-two progressive luma region: four four four has twelve component samples, four two two has eight, and four two zero has six, with chroma positions illustrative only.](https://damjan-popic.github.io/assets/images/agrft/v2/video-chroma.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/video-chroma.svg)

Chroma subsampling stores colour-difference components at a lower spatial sampling density than luma. It takes advantage of the fact that many pictures tolerate less fine colour detail than fine luma detail. It is already a reduction of information, even before a later codec applies lossy quantisation.

For this comparison, use an even-sized **progressive** picture and count samples within a 2 × 2 luma block:

| Sampling | Y′ samples | Cb samples | Cr samples | Total samples | Nominal bits at 8 bits per sample |
| --- | --- | --- | --- | --- | --- |
| 4:4:4 | 4 | 4 | 4 | 12 | 96 |
| 4:2:2 | 4 | 2 | 2 | 8 | 64 |
| 4:2:0 | 4 | 1 | 1 | 6 | 48 |

In 4:2:2, each chroma grid has half the luma width and the full height. In progressive 4:2:0, each has half the width and half the height. The zero in “4:2:0” does **not** mean that the picture has no red-difference channel.

The table describes sampling density, not a universal rule that four finished RGB pixels must be painted the same colour. Conversion normally filters chroma before downsampling. Reconstruction interpolates the chroma grid, and each position retains its own luma. The exact chroma sample locations, called **chroma siting**, differ between formats. Interlaced 4:2:0 needs special care because the vertical structure also interacts with fields.

Reference: [Microsoft, recommended eight-bit video formats and sampling grids](https://learn.microsoft.com/en-us/windows/win32/medfound/recommended-8-bit-yuv-formats-for-video-rendering).

Consider white text with thin saturated-red edges. Luma can preserve much of the text’s shape while the reduced chroma grid blurs or displaces fine colour transitions. A green-screen boundary may become harder to isolate precisely. Increasing a 4:2:0 file to 4:4:4 gives the output more samples, but those new samples are reconstructed estimates. The original missing colour detail does not automatically return.

### Code range and banding

Eight-bit narrow-range video commonly uses **16–235** for nominal black-to-white luma, **16–240** for the nominal chroma range and **128** for neutral chroma. At ten bits the corresponding codes are **64–940**, **64–960** and **512**. The scaling is by four.

| Representation | Nominal luma black | Nominal luma white | Neutral chroma | Nominal chroma endpoints |
| --- | --- | --- | --- | --- |
| 8-bit narrow range | 16 | 235 | 128 | 16 and 240 |
| 10-bit narrow range | 64 | 940 | 512 | 64 and 960 |

The complete ten-bit integer code space is 0–1023. It must not be confused with the nominal image range. Headroom, footroom and reserved transport values depend on the representation and interface. Full-range computer RGB commonly uses the full integer span, but “full” also has interface-specific meanings. Establish exactly what an application or device expects.

If narrow-range black is incorrectly interpreted as full-range RGB code 16 rather than nominal black, the picture can appear lifted and washed out. The opposite mismatch can crush shadows and clip highlights. A range tag describes an interpretation; changing a tag without the appropriate numerical treatment can create an error.

Reference: [EBU R 103 and its Digital Video Levels Explainer](https://tech.ebu.ch/publications/r103).

**Banding** occurs when smooth changes become visible steps. More bits provide finer numerical spacing within a specified representation. They cannot, by themselves, remove sensor noise, restore clipped highlights or reverse an earlier eight-bit bottleneck. Encoding an already damaged gradient in ten bits preserves the damaged gradient more precisely. The practical question is where the first irreversible reduction occurred.

### What uncompressed video actually costs

For an even-sized progressive image without alpha, the nominal sample counts per luma position are three for 4:4:4, two for 4:2:2 and one-and-a-half for 4:2:0. This gives a useful payload calculation:

`bits per second = width × height × frames per second × samples per luma position × bits per sample`

For 1920 × 1080, 25 fps, ten-bit 4:2:2:

`1920 × 1080 × 25 × 2 × 10 = 1,036,800,000 bit/s`

Divide by eight to obtain **129,600,000 bytes per second**, or **129.6 MB/s** in decimal units. Multiply by 3600 for **466.56 GB per hour**.

| Picture representation | Nominal picture rate | Decimal MB/s | Decimal GB/hour |
| --- | --- | --- | --- |
| 1920 × 1080p25, RGB, 8 bits per component | 1.24416 Gbit/s | 155.52 | 559.872 |
| 1920 × 1080p25, Y′CbCr 4:2:2, 10 bits | 1.0368 Gbit/s | 129.6 | 466.56 |
| 1920 × 1080p25, Y′CbCr 4:2:0, 8 bits | 0.62208 Gbit/s | 77.76 | 279.936 |
| 3840 × 2160p25, Y′CbCr 4:2:2, 10 bits | 4.1472 Gbit/s | 518.4 | 1866.24 |

These are calculated **active-picture payloads**, excluding sound, metadata, blanking, transport overhead and padding. They are not the data rates of a named SDI link or compressed codec.

Ten significant bits may occupy sixteen bits in a memory surface. A packed format may arrange samples into larger machine words, and each row may have a padded stride. The nominal bit count and the actual allocated memory can therefore differ. A manufacturer’s memory-format specification is needed for exact buffer sizes; see [Microsoft’s 10-bit and 16-bit layouts](https://learn.microsoft.com/en-us/windows/win32/medfound/10-bit-and-16-bit-yuv-video-formats).

Storage capacity is only one constraint. A drive must sustain the required rate, interfaces must carry it, and the processor must decode and process the stream quickly enough. A small, heavily compressed file can be more demanding to edit than a much larger intraframe file.

### Compression: predict, describe the difference, code efficiently

A video encoder tries to represent useful picture information with fewer bits. A common hybrid coding pipeline predicts a block, subtracts that prediction from the actual block, transforms the remaining difference, quantises transform coefficients and entropy-codes the result. It also writes the information needed to reproduce its choices.

**Prediction** exploits similarity. Intra prediction uses already reconstructed neighbouring information within the same picture. Inter prediction uses reference pictures. **Motion compensation** constructs a prediction from suitably displaced reference-image regions. A motion vector identifies a displacement; it is not necessarily a physical object’s true motion.

The **residual** is the difference between the current samples and the prediction. Imagine that four luma samples are 102, 103, 104 and 104, while the prediction is 100 at all four positions. The residual is 2, 3, 4 and 4. The decoder can add that residual to the same prediction to recover the original samples exactly if those values are preserved.

A real encoder must signal reference choices, block divisions and other decisions. Prediction does not make those costs vanish. A complicated prediction that saves little residual information may cost more bits than a simpler one.

Technical references: [AOMedia, AV1 tool description](https://aomedia.org/docs/AV1_ToolDescription_v11-clean.pdf); [MIT’s StreamIt MPEG-2 encoder description](https://groups.csail.mit.edu/cag/streamit/mpeg/encoder.shtml).

### Transform, quantisation and entropy coding

A **transform** changes the coordinates in which a block is described. A DCT-like transform represents spatial patterns through coefficients associated with different frequencies. A smooth block can concentrate much of its information in relatively few coefficients. The transform is not, by itself, a command to throw information away.

**Quantisation** reduces precision. In a simplified scalar example, dividing coefficients 23, 6 and −2 by a step of 8 and rounding to the nearest integer gives 3, 1 and 0. Multiplying back by 8 reconstructs 24, 8 and 0. The original values have changed. The zero can be particularly economical to code, but −2 cannot be recovered exactly from it.

The step size and quantisation decisions affect the trade-off between detail and data rate. Aggressive choices can produce block boundaries, ringing around edges, banding or loss of moving texture. Actual codecs have more elaborate transforms, quantisers, prediction modes and loop filters than this miniature example.

**Entropy coding** then represents symbols according to their statistical structure. Frequent or predictable patterns can be represented efficiently. This stage is reversible: it must recover the coded symbols exactly. In a conventional lossy pipeline, the irreversible reduction has already occurred through operations such as quantisation or subsampling.

The encoder usually reconstructs its own coded reference pictures so that its future predictions match the decoder’s references. Predicting from an original picture that the decoder never received would allow their states to diverge.

References: [CMU, video compression lecture](https://graphics.cs.cmu.edu/courses/15869/fall2013content/lectures/20_videocompression/videocompression_slides.pdf); [ITU-T H.264](https://www.itu.int/rec/T-REC-H.264); [AOMedia’s AV1 specification](https://aomedia.org/specifications/av1/).

### I, P and B pictures: why playback order can differ

![A four-picture GOP displayed as I0 B1 B2 P3, reference relationships from I0 and P3 to B1 and B2, and a valid decode order I0 P3 B1 B2. B pictures are non-reference only in this example.](https://damjan-popic.github.io/assets/images/agrft/v2/video-gop.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/video-gop.svg)

**Intraframe** coding represents a picture without inter-picture prediction. **Interframe** coding permits prediction from other pictures. The traditional I/P/B terminology distinguishes picture or slice prediction capabilities, although the precise structures vary between codecs.

An I picture is intra-coded. A P picture permits prediction using reference information from one reference list. A B picture permits prediction using two reference lists. The familiar beginner’s example gives a B picture both an earlier and a later displayed reference, but actual reference arrangements can be more varied.

Consider this deliberately small example:

| Display position | Picture | References used in this example |
| --- | --- | --- |
| 0 | I0 | None |
| 1 | B1 | I0 and P3 |
| 2 | B2 | I0 and P3 |
| 3 | P3 | I0 |

To display B1, the decoder already needs P3. A suitable decoding order is therefore **I0, P3, B1, B2**, while display order remains **I0, B1, B2, P3**. Buffers and timestamps coordinate the two orders. B1 and B2 are not reference pictures in this example; modern coding can also use B pictures as references.

A **group of pictures**, or **GOP**, describes a related picture structure. Longer dependencies can improve compression but complicate seeking, recovery after errors and frame-accurate editing. An I picture is not automatically a completely independent starting point for everything that follows. An **IDR** picture in AVC provides a specified decoder refresh behaviour; random-access rules need more precision than “there is an I-frame”.

References: [ITU-T H.264](https://www.itu.int/rec/T-REC-H.264); [RFC 6184, H.264 access units, decoding order and transport](https://www.rfc-editor.org/rfc/rfc6184.html).

### Lossless, lossy and visually lossless video

**Mathematically lossless** coding reconstructs exactly the sample values supplied to that coding process. **Lossy** coding permits different reconstructed values. **Visually lossless** describes an intended or assessed visual result under stated viewing conditions; it does not guarantee numerical identity.

Suppose a 4:4:4 image is first converted to 4:2:0 and then compressed with a mathematically lossless codec. The codec can preserve the 4:2:0 samples exactly. It does not reverse the earlier subsampling. Likewise, a lossless file made from an analogue capture preserves the captured numerical representation, not every property of the original electrical waveform.

**FFV1** is a lossless intraframe video format specified in [RFC 9043](https://www.rfc-editor.org/rfc/rfc9043.html). **ProRes** is an intraframe codec family whose image coding is generally lossy; Apple describes suitable variants as visually lossless. The alpha channel in ProRes 4444 has separate lossless behaviour. A statement about alpha must not be extended to all picture components.

A high-quality master can legitimately use a lossy professional codec if that matches the agreed workflow. A preservation decision asks a different question: which properties and evidence must remain recoverable, and which transformations are acceptable? Always name the actual codec variant and representation.

Reference: [Apple ProRes white paper](https://www.apple.com/final-cut-pro/docs/Apple_ProRes.pdf).

### Codec families and their purposes

The following is a working map, not a ranking. A codec name alone does not specify quality, colour space or editing performance.

| Codec or family | Where it is encountered | What to establish |
| --- | --- | --- |
| MPEG-2 Video / H.262 | Legacy broadcast, DVD-Video and archives | Profile, rate, dimensions and scan structure |
| H.264 / AVC | Camera recording, web delivery and broadcast | Profile, level, bit depth, chroma and GOP structure |
| H.265 / HEVC | Efficient high-resolution and HDR delivery; recording | Decoder support for the actual profile and representation |
| AV1 | Efficient distribution and streaming | Encoder configuration and device decoding support |
| Apple ProRes | Camera and post-production workflows | Proxy, LT, 422, HQ, 4444 or 4444 XQ; alpha where relevant |
| Avid DNxHD / DNxHR | Editing and mastering | Exact quality variant, sampling and component precision |
| FFV1 | Lossless storage and audiovisual preservation | Version, pixel format, metadata and validation |
| JPEG 2000 | Digital cinema and some preservation workflows | Specified profile, colour representation and lossless/lossy mode |

A **profile** identifies an allowed subset of coding features. A **level** constrains quantities such as picture size, processing rate and decoder resources. “The computer plays H.264” is incomplete if it can decode one profile but not the ten-bit 4:2:2 material supplied.

References: [ITU, HEVC](https://www.itu.int/rec/T-REC-H.265); [AOMedia, AV1](https://aomedia.org/specifications/av1/); [Avid, DNxHR specifications](https://kb.avid.com/pkb/articles/en_US/Knowledge/DNxHR-Codec-Bandwidth-Specifications); [DCI specifications](https://www.dcimovies.com/dci-specification/).

Hardware video decoders are specialised processing blocks. Their supported combinations depend on the hardware generation and software path. A powerful GPU does not imply universal codec support. The question is whether that decoder supports this codec, profile, chroma format, precision, picture size and rate. See [NVIDIA’s decoder capability documentation](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.1/nvdec-application-note/index.html) for a manufacturer’s example.

### Containers, image sequences and rewrapping

A **container** organises encoded media streams and their timing. An MP4 might contain AVC video, AAC sound and other tracks; a MOV might contain ProRes and PCM sound. These are examples, not exclusive pairings. MXF supports professional media exchange through specified operational patterns and mappings. Matroska can carry multiple audio, video and subtitle tracks.

A file extension identifies a likely container, not the entire technical specification. Renaming `.mov` to `.mp4` does not change the container structure or re-encode the picture.

**Rewrapping**, or **remuxing**, moves compatible encoded streams into another container without decoding and re-encoding their pictures. **Transcoding** changes the encoded representation. It generally requires decoding and encoding, potentially with changes to sampling, precision, colour or timing. Rewrapping may still alter file bytes and metadata even though the coded picture stream remains unchanged.

An **image sequence** stores pictures in separate files, commonly using formats such as DPX or OpenEXR. OpenEXR can store multiple channels and floating-point samples, including image information useful for visual effects. It supports different compression methods; the extension alone does not establish mathematical losslessness. A sequence also needs frame-order and frame-rate information, and sound usually accompanies it separately.

References: [FFmpeg’s description of stream copying](https://ffmpeg.org/ffmpeg.html#Streamcopy); [OpenEXR technical introduction](https://openexr.com/en/latest/TechnicalIntroduction.html).

### From the coded bits back to a picture

During playback, a demultiplexer finds the video stream and its timing. The decoder then reads the syntax of that coding format. In AVC, for example, network abstraction layer units carry different types of information, including parameters and coded slices. A container boundary, a packet boundary, a coded-picture boundary and a displayed-frame boundary are not necessarily the same thing.

The decoder obtains prediction decisions and coded residual information, reconstructs coefficients, applies the inverse transform, adds the prediction and performs the specified filtering. Reconstructed pictures may enter a reference buffer as well as the display queue. Colour conversion and display rendering then produce the values needed by the output system.

Consequently, locating the twenty-four binary RGB digits in the earlier pixel example inside a compressed MP4 is generally not a meaningful search. Compression has reorganised the representation. The decoder has to interpret that representation before those output samples exist.

Reference: [RFC 6184, AVC structure and terminology](https://www.rfc-editor.org/rfc/rfc6184.html).

### Bit rate, quality and streaming

**Bit rate** is the amount of encoded data per second. **Constant bit rate**, **variable bit rate** and quality-targeted encoding describe different allocation strategies. Exact behaviour depends on the encoder and its buffer constraints.

At an average video rate of 20 Mbit/s, ten minutes of video payload requires:

`20,000,000 × 600 ÷ 8 = 1,500,000,000 bytes = 1.5 GB`

Add audio and container overhead for the complete file. The result is an estimate when 20 Mbit/s is a target rather than a measured average.

The same bit rate can produce different visible quality with different codecs, encoders and images. A locked-off interview against a plain wall is easier to predict than handheld movement through detailed foliage. Grain, noise, water, smoke and confetti can make compression demanding. The number of pixels does not tell us how much unpredictable information they contain.

Streaming services commonly prepare several encoded renditions. A player requests short segments and changes rendition as network and playback conditions change. A playlist or manifest describes available media and segment locations. The viewer may therefore receive a different bit rate or resolution at different moments. **Streaming** names a delivery arrangement, not one codec.

Reference: [RFC 8216, HTTP Live Streaming](https://www.rfc-editor.org/rfc/rfc8216.html).

The transition from physical video carriers to network delivery did not remove compression. Video CD used MPEG-1; DVD-Video commonly uses MPEG-2; conventional Blu-ray supports defined MPEG-2, AVC and VC-1 video options. Modern distribution adds newer codecs and delivery systems. The medium and the encoding remain separate choices. References: [Library of Congress, Video CD](https://wwws.loc.gov/marc/marbi/2002/2002-dp01.html); [Library of Congress, MPEG-2](https://www.loc.gov/preservation/digital/formats/fdd/fdd000335.shtml); [Sony, Blu-ray codecs](https://www.sony.com/electronics/support/home-video-blu-ray-disc-players-recorders/uhp-h1/articles/00029663).

### Colour management: numbers need the right destination

A colour description must distinguish **primaries**, **transfer function**, **matrix coefficients** and **range**. The primaries define the colour basis. The transfer function relates encoded values to a light-related domain. The matrix specifies conversion between component representations such as RGB and Y′CbCr. Range specifies numerical scaling.

A camera’s **log** encoding redistributes code values over a broad scene range. Log footage commonly appears low in contrast when displayed without the intended conversion. The required transform depends on the actual log curve and camera colour space. “Apply a log LUT” is too vague: a LogC3 transform is not automatically appropriate for LogC4, and neither is a universal transform for other manufacturers’ log formats.

A **LUT**, or look-up table, maps input values to output values. It may implement a technical conversion, a creative look or a combination. Its intended input and output must be known. Applying an output transform twice can distort an otherwise correct image.

Reference: [ARRI, Log C and display transforms](https://www.arri.com/en/learn/camera-systems/image-science/log-c).

**HDR**, high dynamic range, concerns the represented and displayed light range. **Wide colour gamut** concerns the available colour range. **UHD** concerns image dimensions. These properties can occur together but are not synonyms. Ten-bit precision alone does not make material HDR.

BT.2100 specifies both **PQ** and **HLG** HDR systems. PQ defines a perceptually shaped mapping associated with absolute display luminance, with a formal upper scale of 10,000 cd/m². This does not mean every PQ master or display reaches 10,000 cd/m². HLG combines a scene-related encoding with a display system whose rendering depends on the intended viewing arrangement. A colour-managed conversion is required; replacing an HDR tag with “Rec.709” does not correctly turn HDR into SDR.

Reference: [ITU-R BT.2100-3](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2100-3-202502-I!!PDF-E.pdf). Monitor behaviour and viewing conditions matter as well; see [EBU Tech 3320](https://tech.ebu.ch/publications/tech3320).

### Frame rate, exposure time and retiming

**Frame rate** says how often pictures occur. **Exposure time** says how long a camera collects light for a picture or sensor row. They affect motion differently.

At 25 fps, one frame interval is 40 ms. An exposure of 1/50 s collects light for 20 ms of that interval. An exposure of 1/250 s collects light for 4 ms. Both recordings may still contain 25 frames per second, but moving objects have different motion blur. The camera chapter develops the equivalent shutter-angle calculation.

Changing the playback rate is another operation. Fifty acquired frames played at 25 fps occupy two seconds, so one second of acquisition becomes two seconds of playback. A 25 fps recording converted to 50 fps at its original duration instead requires duplicated or synthesised output pictures. It has not acquired new observations of the scene. Motion interpolation estimates intermediate images and can fail at occlusions, fine structures and complex motion.

The commonly rounded rates **23.976**, **29.97** and **59.94** usually mean **24000/1001**, **30000/1001** and **60000/1001** respectively. Exact 24 and 24000/1001 are different rates. A mismatch can accumulate over a long programme even when a short clip appears satisfactory.

Reference: [Apple, frame-size and frame-rate conforming](https://support.apple.com/en-ca/guide/final-cut-pro/ver3363b44e/mac).

With **constant frame rate**, successive presentation times follow a uniform interval. **Variable frame rate** permits unequal intervals; an average reported as “30 fps” does not establish the timing of every picture. Frame timestamps therefore matter. A conversion to constant frame rate must map the original timing to a new grid while preserving the intended duration and sound relationship. VFR and variable **bit** rate are different properties: one concerns picture timing, the other data allocation. See [Adobe’s VFR explanation](https://community.adobe.com/questions-729/faq-how-to-work-with-variable-frame-rate-vfr-media-in-premiere-pro-1349720).

### Timecode, synchronisation and proxies

**Timecode** assigns addresses to frames. A label such as `01:00:00:00` need not mean that the file has already played for an hour; it may be the chosen starting address. Always establish the rate, starting address and counting convention.

At 25 fps, the final pair of timecode digits ranges from 00 to 24. With an inclusive in-point and an exclusive out-point, the interval from `01:00:10:00` to `01:00:12:10` contains **60 frames**, or **2.4 seconds**.

At 30000/1001 fps, **drop-frame timecode** skips specified labels to keep the count close to clock time. It skips labels 00 and 01 at the start of each minute except minutes divisible by ten. Actual video frames are not discarded. The sequence `00:00:59;29` is followed by `00:01:00;02`; `00:09:59;29` is followed by `00:10:00;00`. A semicolon commonly identifies drop-frame notation.

Reference: [Apple, timecode support and drop-frame counting](https://developer.apple.com/library/archive/technotes/tn2310/_index.html).

**Synchronisation** also concerns clocks. A fixed audio offset and a steadily increasing drift have different causes and require different corrections. Moving audio by a constant amount can fix a constant offset; it cannot by itself correct a duration mismatch.

**Genlock** synchronises video timing to a reference. Matching timecode addresses alone does not establish that different cameras expose or output their frames at exactly the same phase. Some cameras can derive synchronisation from a timecode signal under specified operating modes; check the camera’s actual capabilities. See [ARRI, synchronisation with external devices](https://www.arri.com/resource/blob/233578/1834cdca3692ee85ffc5f09ebca74ae0/2024-10-mrps-synchronization-of-arri-cameras-ti-data.pdf).

A **proxy** is a linked working representation used to make editing easier. It may reduce image dimensions, bit rate or decoding complexity. The link must preserve the correspondence between source and working frames. Frame rate, duration, timecode, identifiers and audio structure matter when reconnecting originals for finishing. A good-looking offline edit is not proof that the final conform will reconnect correctly. Reference: [Adobe, ingest and proxy workflows](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html).

### Describing a video problem precisely

“Bad quality” does not identify a mechanism. State what you observe, where it occurs and what you have checked.

| Observation | Precise English description | Relevant distinction to investigate |
| --- | --- | --- |
| Moving edges show teeth | “There is combing on motion.” | Fields, field order and deinterlacing |
| Dark areas have become grey | “The black level appears lifted.” | Range interpretation and display transform |
| A smooth sky has steps | “There is visible banding in the gradient.” | Precision, processing and compression |
| Blocks appear in moving texture | “Compression artefacts increase during movement.” | Bit allocation, prediction and quantisation |
| Sound falls progressively behind | “The sync error increases over time.” | Clock or duration mismatch |
| Titles have coloured fringes | “Fine chroma edges are displaced or softened.” | Chroma sampling, siting and reconstruction |
| An export looks flatter than the timeline | “The display rendering differs between the two views.” | Colour metadata, transforms and playback environment |

These are hypotheses to investigate, not diagnoses guaranteed by the visible symptom. Comparing the source, timeline and export under the same viewing conditions helps locate the change.

### Terms to use accurately

| English term | Slovene orientation | Meaning to retain |
| --- | --- | --- |
| frame | sličica; pri filmu tudi fotogram | One complete picture unit in the specified sequence |
| field | polslika | One of the alternating-line components of interlaced video |
| raster | raster | Organised picture-sampling or scanning grid |
| blanking interval | zatemnitveni interval | Non-active interval associated with scanning and timing |
| sync pulse | sinhronizacijski impulz | Timing reference in a signal |
| colour burst | barvni sinhronizacijski paket | Subcarrier reference in PAL/NTSC composite systems |
| luma | luma | Weighted non-linear video component Y′ |
| luminance | svetlost v kolorimetričnem pomenu | Defined light-related quantity; distinguish it from luma |
| chroma subsampling | podvzorčenje barvnih komponent | Reduced sampling density of colour-difference components |
| bit depth | bitna globina | Number of bits used for a component sample |
| bit rate | bitna hitrost | Encoded or transmitted bits per second |
| field order | vrstni red polslik | Which field occurs first in time |
| deinterlacing | razpletanje prepletene slike | Reconstruction of progressive output from interlaced input |
| time-base correction | korekcija časovne baze | Correction of playback timing irregularities |
| residual | ostanek; razlika glede na napoved | Difference between an actual block and its prediction |
| reference picture | referenčna slika | Reconstructed picture used in prediction |
| rewrap / remux | ponovno oviti; ponovno multipleksirati | Change compatible packaging without re-encoding pictures |
| transcode | prekodirati | Change the coded representation |
| conform | uskladiti montažo z izvornim gradivom | Reconstruct the edit using the intended source media |
| preservation master | ohranitvena matična datoteka | Documented file retained to preserve the source representation |

**Model handover:** “This is the capture master, preserving the source field order. I have made a separate progressive viewing copy. The master uses ten-bit 4:2:2 FFV1 in Matroska, with the colour interpretation and audio settings documented. The viewing copy uses a delivery codec and should not replace the master.”

The model specifies a coherent example, not a compulsory institutional capture standard. The required master, working copy and delivery file must be agreed for each production or collection.

## 4. How cameras form and record images

A camera connects the physical world to the computer. Light carries information about a scene. The lens forms an image; the sensor makes electrical measurements of that image; the camera processes and encodes those measurements. The recording medium stores a file that editing software can interpret.

These are different operations. A lens does not produce pixels. A photodiode does not produce a finished colour picture. A memory card does not determine the camera's dynamic range. Describing the complete route accurately requires us to identify what enters each component, what changes there, and what leaves it.

The explanations below use a conventional single-sensor digital camera as their starting point. Other designs are identified where they change the explanation. Optical drawings are either explicitly defined mathematical models or functional diagrams. They are not manufacturing drawings of the particular camera used in class.

### The camera in front of us

Start with the outside. Name each part, locate it, and explain its function before discussing its specifications. A useful description is: “The lens mount is the interface at the front of the body. It secures the lens and establishes its position relative to the sensor.”

| Part | Function | Slovene orientation |
|---|---|---|
| Camera body | Houses the sensor, processing electronics, controls and recording connections. | ohišje kamere |
| Lens / lens assembly | Forms an optical image through a combination of lens elements. The complete photographic lens is an objektiv; an individual element is a leča. | objektiv / sklop leč |
| Lens mount | Provides the mechanical interface between lens and body; many mounts also carry electrical contacts. | bajonet oziroma priključek objektiva |
| Mount locking ring / release | Secures or releases a compatible lens. The mechanism depends on the mount. | zaklepni obroč / sprostitev objektiva |
| Focus ring | Changes the lens's focusing configuration. | obroč za ostrenje |
| Zoom ring | Changes focal length on a zoom lens. | obroč za spreminjanje goriščnice |
| Iris ring / aperture control | Sets the aperture through a mechanical linkage or electronic command. | obroč oziroma upravljanje zaslonke |
| Lens hood | Shades the front of the lens from unwanted off-axis light. | sončna zaslonka |
| Matte box | Holds filters and, with its shade and flags, controls unwanted light entering the lens. | kompendij / nosilec filtrov s senčilom |
| Follow focus | Transfers movement from a handwheel or motor to the lens's focus mechanism. | mehanizem za upravljanje ostrenja |
| Lens support and support rods | Carry accessory or lens loads through the rig rather than leaving the mount to carry every load. | podpora objektiva in nosilne cevi |
| Sensor-plane mark | Identifies the image-plane position used as a distance reference. | oznaka ravnine tipala |
| Electronic viewfinder / EVF | Displays an electronic monitoring image close to the operator's eye. | elektronsko iskalo |
| On-board monitor | Shows framing, status information and monitoring tools. | monitor na kameri |
| Record button / tally light | Starts or stops recording; the tally indicates a recording or live status according to the system. | tipka za snemanje / signalna lučka |
| Media slot | Accepts a supported recording card or module. | reža za snemalni nosilec |
| Battery plate / power input | Connects a battery or an external power supply. | baterijska plošča / napajalni priključek |
| SDI / HDMI output | Carries a specified video signal to compatible equipment; supported formats depend on the device and interface version. | videoizhod SDI / HDMI |
| Microphone / line input | Receives audio at the appropriate signal level. | mikrofonski / linijski vhod |
| Headphone output | Lets the operator monitor the audio signal routed to it. | izhod za slušalke |
| Timecode connection | Exchanges timecode for identification and synchronization workflows. | priključek za časovno kodo |
| Genlock input | Accepts a reference that can align camera video timing in a compatible system. | vhod za sinhronizacijski signal |
| USB / Ethernet connection | May carry control, data, networking or power, depending on the implementation. | povezava USB / Ethernet |
| Baseplate / tripod plate | Connects the camera rig to its support. | osnovna / stativska plošča |
| Heat sink, vents and fan | Conduct heat away from electronics and exchange it with the surrounding air. | hladilno telo, zračniki in ventilator |

Do not infer a connection's entire function from its shape. A BNC socket may be SDI, timecode or reference; the label and manual settle the question. “This cable fits” is a mechanical observation. “This output supplies the required signal” is a technical conclusion.

The mount also establishes **flange focal distance**: the specified distance from the mount's reference surface to the image plane. This is different from focal length. Incorrect spacing can prevent a lens from reaching the expected focus or make its distance markings unreliable. ARRI's published mount descriptions show why mechanical alignment belongs in an explanation of image quality. Its accessory documentation also distinguishes lens support, follow focus and matte-box functions. [ARRI: lens mounts](https://www.arri.com/en/learn/arri-camera-technology/lens-mounts-and-lds-2), [follow focus](https://www.arri.com/en/cine-systems/mechanical-accessories/follow-focus), [matte boxes](https://shop.arri.com/Products/PCA-Mechanical-Accessories/Matte-Boxes/).

### How a lens forms an image

An illuminated point on a subject sends light in many directions. The camera captures only part of that light. A small pinhole can form an image by admitting a narrow selection of rays from each point; a lens admits a much larger bundle and brings it towards the corresponding image point.

A transparent lens changes the direction of light by **refraction** at its surfaces. A converging lens can bring rays from a distant point to a focus. For an ideal thin lens in air, focal length is the distance from the lens plane to the focus of incoming rays parallel to the optical axis. Real photographic lenses contain several elements and groups: their focal length is defined using principal planes, which need not coincide with a visible glass surface.

![Exact paraxial thin lens ray construction with focal length fifty millimetres, object distance two hundred millimetres, image distance sixty-six and two-thirds millimetres, object height twenty and inverted image height six and two-thirds millimetres, equal axis scales.](https://damjan-popic.github.io/assets/images/agrft/v2/camera-optical-path.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/camera-optical-path.svg)

The ray diagram uses an ideal positive thin lens:

- Focal length, f = 50 mm.
- Object distance, u = 200 mm.
- Object height, h = 20 mm.
- Image distance, v = 66.67 mm.
- Image height, h′ = −6.67 mm.

The thin-lens equation is **1/f = 1/u + 1/v**. Therefore v = fu/(u − f) = 50 × 200/150 = 66.67 mm. Magnification is m = −v/u = −1/3. The minus sign describes inversion: the top of the object is imaged below the optical axis. The camera's display and file interpretation provide the intended viewing orientation.

Trace three rays from the top of the object. A ray parallel to the axis bends through the image-side focal point. A ray through the lens centre continues undeviated in this thin-lens approximation. A ray through the object-side focal point emerges parallel to the axis. They intersect at the same image point. They are selected construction rays from a much larger bundle, not three special beams that alone make the photograph.

These equations are a first-order model. They neglect lens thickness, aberrations and diffraction. Do not use the diagram's 66.67 mm as a camera mount specification. With a real lens, focusing may move one group, several groups or the entire optical assembly. [Edmund Optics: forming an image](https://www.edmundoptics.com.tw/knowledge-center/video/tutorials/how-to-form-an-image-with-an-optical-lens-setup/).

**Focal length and framing.** For an ideal rectilinear lens focused at infinity, horizontal angle of view is approximately **2 arctan(w / 2f)**, where w is the active image width. A 50 mm lens across 36 mm gives about 39.6°. Across 24 mm it gives about 27.0°. State the dimension: horizontal, vertical and diagonal angles differ.

This calculation explains a sensor crop. The same lens still has a focal length of 50 mm, but a smaller active region records a narrower portion of its image. The active recording area matters: a camera may use different crops for different modes. A lens also needs an **image circle** large enough to cover that area. [Edmund Optics: focal length and field of view](https://www.edmundoptics.com/knowledge-center/application-notes/imaging/understanding-focal-length-and-field-of-view/), [ZEISS: image-circle coverage](https://lenspire.zeiss.com/cine/en/article/large-image-circle-universal-usability-the-compact-prime-cp-3-and-cinema-zoom-cz-2-lens-families).

Perspective depends on viewpoint. Cropping a picture from a fixed camera does not change the relative geometry within the retained image. If you move the camera to restore a person's original size after changing focal length, you also change the viewpoint, and therefore the relationship between near and distant objects. Describe both actions: “We changed from 25 mm to 50 mm and moved the camera farther back.”

A **prime lens** has one focal length; it can still focus at different distances. A **zoom lens** offers a range of focal lengths. A **parfocal** lens is designed to maintain focus while zooming under its specified conditions. A varifocal lens changes focus as focal length changes. Do not assume every lens sold as a zoom maintains critical cinema focus without adjustment.

An **anamorphic lens** has different image magnification in the horizontal and vertical directions. A stated 2× horizontal squeeze requires the corresponding de-squeeze for intended proportions. If the recorded picture has a 1.20:1 aspect ratio and square pixels, a 2× horizontal de-squeeze produces 2.40:1 before any further crop. This is geometry, not video compression: an optical squeeze is different from a codec removing or predicting data. Choose the lens, active recording area and monitoring de-squeeze together. A 16:9 frame with a 2× squeeze would yield about 3.56:1 before cropping, so an anamorphic lens does not automatically create a 2.39:1 deliverable. [ARRI: anamorphic formats](https://www.arri.com/en/learn-help/learn-help-camera-system/frequently-asked-questions/alexa-sxt-faq/why-6-5-i-thought-you-needed-4-3-for-anamorphic--41676), [ARRI: monitoring de-squeeze](https://www.arri.com/resource/blob/374970/87726e6d9ad7fe7c2e8d80b79e157a5f/2024-05-22-ccm-1-anamorphic-desqueeze-quickguide-en-data.pdf).

### Aperture, f-stops, T-stops and neutral density

The **aperture** is the opening that limits the light bundle. The **iris** is the mechanism, usually overlapping blades, that varies that opening. Looking through the front of a lens, we see an optical image of the aperture stop: the **entrance pupil**. Its diameter, rather than the bare mechanical hole measured inside a complex lens, is used in the conventional f-number.

**N = f / D**, where N is f-number, f is focal length and D is entrance-pupil diameter. At 50 mm and f/2, D = 25 mm. At f/4, D = 12.5 mm. Halving the diameter quarters the area. Consequently, f/2 to f/4 reduces illumination by two stops, assuming other relevant factors remain constant.

![Four precisely area-scaled circular entrance pupils at constant focal length corresponding to f two, f two point eight, f four and f five point six, with relative areas one one-half one-quarter one-eighth.](https://damjan-popic.github.io/assets/images/agrft/v2/camera-stops.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/camera-stops.svg)

The full-stop sequence is conventionally written **f/1, f/1.4, f/2, f/2.8, f/4, f/5.6, f/8, f/11, f/16, f/22**. The unrounded sequence increases by √2 each time. Because area depends on diameter squared, each step towards a larger f-number halves the admitted light in the ideal comparison. Values such as 2.8 and 5.6 are convenient rounded labels. Lens transmission and close-focus effects require additional care in precision work. [Edmund Optics: f-number and throughput](https://www.edmundoptics.com/knowledge-center/application-notes/imaging/lens-iris-aperture-setting/).

For the same scene and lens, a useful comparison is:

**sensor exposure ∝ transmission × exposure time / f-number².**

Here exposure means light delivered per unit sensor area during the integration interval. The expression is a comparison model, not a complete radiometric description of vignetting, close-up optics or every point in the frame.

A **T-stop** includes measured light transmission. If τ is the fraction transmitted by the lens, then **T = N / √τ**. Consider a lens at f/2 with τ = 0.81. Its T-number is 2/0.9 = 2.22. A lossless ideal lens at f/2.22 would deliver the same exposure under the assumed conditions. The physical entrance pupil of the first lens has not become that of an f/2.22 lens: transmission and geometry are distinct.

T-stops help match exposure when changing cinema lenses. They do not make different lenses identical in depth of field, flare or rendering. In ordinary shooting, follow the scale and calibration intended for that lens. [Canon: cinema-lens features and T-stops](https://snapshot.asia.canon/en/article/videography-faq-should-i-invest-in-a-cinema-lens).

A **neutral-density filter**, or ND, attenuates light. It lets you retain an aperture and exposure duration that suit the picture while reducing sensor exposure. Optical density d is defined by **d = −log10(τ)**, so transmission is **τ = 10^(−d)**. The number of stops removed is **s = log2(1/τ) = d / log10(2)**.

| Common density label | Approximate transmission | Conventional reduction |
|---|---:|---:|
| ND 0.3 | 50% | 1 stop |
| ND 0.6 | 25% | 2 stops |
| ND 0.9 | 12.5% | 3 stops |
| ND 1.2 | 6.3% | 4 stops |
| ND 1.8 | 1.6% | 6 stops |

These density labels are rounded: exact one-stop density is approximately 0.30103. A filter-factor label such as **ND8** commonly means 1/8 transmission, or three stops; it does not mean optical density 8. Read the maker's notation.

“Neutral” is the intended spectral behaviour. Real filters can alter colour, and heavy visible-light attenuation may expose infrared contamination in some camera systems. IRND filters address infrared transmission as well. A variable ND is an adjustable attenuation system; its mechanism, range and artefacts depend on the design. Test a physical filter at the settings you will use. [Tiffen: ND 0.6](https://tiffen.com/products/tiffen-5-x-6-nd-0-6-filter-2-stop), [Tiffen: ND and IRND products](https://flysteadicam.tiffen.com/collections/neutral-density-filters).

**Worked decision.** A setup is correctly exposed at f/8, 1/50 s. You want f/2.8 to reduce depth of field, keeping the same exposure duration and gain mode. Opening f/8 → f/5.6 → f/4 → f/2.8 adds three stops. Add approximately three stops of ND, conventionally ND 0.9, to retain the original sensor exposure. You have changed the geometry of the light bundle while restoring its total exposure.

### Focus and the limits of sharpness

Focus is the adjustment that places the image of a chosen object plane at the sensor plane. A point away from that chosen plane produces a finite blur patch there. **Depth of field** is the range of object distances whose blur is accepted as sufficiently small for a specified viewing or output condition.

The acceptance criterion matters. A frame may look sharp on a small monitor and reveal missed focus when projected. A depth-of-field table incorporates a chosen **circle of confusion**: a limit for the diameter of acceptable defocus blur in the image. It does not discover a physical boundary at which the scene suddenly changes from sharp to unsharp.

For a fixed lens, focus distance and acceptance criterion, stopping down generally increases depth of field. At a fixed f-number and focal length, focusing closer generally reduces it. Comparisons involving different sensor sizes or focal lengths must state whether viewpoint, subject size, output size and f-number remain constant. “A large sensor has less depth of field” leaves too many variables unstated. [Canon: depth of field](https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/depth-of-field/index.html).

**Depth of focus** refers to tolerance around the image plane, on the sensor side of the lens. It is not another name for depth of field in the scene. The distinction explains why mount alignment and focus marks matter. [Edmund Optics: depth of field and depth of focus](https://www.edmundoptics.eu/knowledge-center/application-notes/imaging/depth-of-field-and-depth-of-focus/).

A focus pull transfers critical focus during a shot. The first camera assistant needs distances, movement timing and an image on which to judge the result. **Focus breathing** is a change in framing or angle of view associated with a focus change. **Bokeh** describes the character of out-of-focus rendering; “more bokeh” is a less precise statement than “a more strongly blurred background.”

Autofocus estimates a suitable lens position. Contrast detection searches for an image condition with strong local contrast. Phase detection compares views through different parts of the pupil to estimate focus error. Subject recognition can choose which subject to follow; it is a separate decision from the optical measurement of focus. Canon's Dual Pixel explanation is one implementation of image-plane phase detection, not a description of every autofocus camera. [Canon: Dual Pixel CMOS AF](https://www.usa.canon.com/learning/training-articles/training-articles-list/canon-autofocus-series-dual-pixel-cmos-af-explained).

Stopping down indefinitely does not make every image sharper. **Diffraction** spreads light even through ideal optics. For an ideal circular aperture, the Airy-pattern central-disc diameter at the image plane is approximately **2.44 × wavelength × f-number**, under the usual paraxial assumptions. At 0.55 μm and f/8, that is 10.7 μm; at f/16, 21.5 μm. These are first-dark-ring diameters, not a universal “smallest visible object” or a binary sharpness threshold.

Thus aperture can improve defocus tolerance while reducing fine-detail contrast through diffraction. Actual performance also includes aberrations, sensor sampling and processing. A focus problem, camera shake, motion blur and compression damage require different diagnoses. [Edmund Optics: the Airy disk and diffraction limit](https://www.edmundoptics.com/knowledge-center/application-notes/imaging/limitations-on-resolution-and-contrast-the-airy-disk/).

### What a film camera changes

A motion-picture film camera forms an optical image too, but records it through a photosensitive emulsion. Exposure produces a latent image that laboratory processing develops into a visible one. A film **magazine** supplies and receives film; the **gate** defines and supports the exposure area; the **pressure plate** helps hold the film in its intended plane. An intermittent transport advances the film between exposures. Where fitted, registration pins help position it accurately. The shutter blocks the light while the film moves.

A reflex mirror-shutter system can direct the lens image towards an optical viewfinder during the closed part of the cycle. Its mechanism differs from an electronic viewfinder displaying a sensor-derived image. Film grain is not a fixed rectangular array of digital pixels. When developed film is scanned, a scanner illuminates it and measures the transmitted image with an electronic sensor; digitization occurs in that later system. Film capture and analogue electronic video are distinct recording methods, even when both ultimately feed a digital edit. [Kodak: Essential Reference Guide for Filmmakers](https://www.kodak.com/content/products-brochures/Film/kodak-essential-reference-guide-for-filmmakers.pdf).

### Inside the sensor: light, charge, voltage and bits

The sensor sits at the image plane. Before light reaches its sensitive regions, it may pass through protective glass, an infrared-cut filter, an **optical low-pass filter**, a colour-filter array and microscopic lenses. A low-pass filter reduces optical detail likely to alias against the sampling grid. An IR-cut filter limits unwanted infrared response. Not every camera uses the same filters, and some omit an optical low-pass filter. A functional diagram cannot establish the exact physical order or construction of every camera's filter stack. [ARRI: sensors and optical low-pass filtering](https://www.arri.com/en/learn/arri-camera-technology/alev-sensors).

A **photodiode** is a semiconductor light detector. Absorbed photons can generate mobile charge carriers. The sensor collects charge during an integration interval. **Quantum efficiency** describes the relationship between incoming photons and detected photoelectrons, usually as a wavelength-dependent efficiency. A larger signal begins here as a larger collected charge, not as a larger binary number. [Hamamatsu: quantum efficiency in camera simulation](https://www.hamamatsu.com/sp/sys/en/camera_simulator/index.html).

In a common CMOS active-pixel architecture, a transfer gate moves collected charge to a readout node. The charge changes that node's voltage; pixel and column circuitry buffer and measure the signal. Reset and reference measurements help distinguish the light-generated signal from electrical offsets. This is an architectural explanation: shared pixels, global-shutter storage and other designs arrange the circuitry differently. [Fossum and Hondongwa: pinned-photodiode operation](https://ericfossum.com/Publications/Papers/2014%20JEDS%20Review%20of%20the%20PPD.pdf), especially the CMOS pixel description on printed p. 35.

A CCD uses a different readout principle: charge packets are shifted through the device towards an output stage. CMOS designs normally provide more local readout circuitry and flexible addressing. Both start from light-generated charge and require a conversion process before digital storage. CCD does not mean “analogue camera,” and CMOS does not mean “rolling shutter.” [Nikon MicroscopyU: CCD operation](https://www.microscopyu.com/tutorials/full-frame-ccd-operation), [Hamamatsu: CMOS sensor development](https://hub.hamamatsu.com/us/en/technical-notes/image-sensors/advances-in-cmos-image-sensors.html).

An **analogue-to-digital converter**, or ADC, maps the measured analogue signal into numerical codes. Some sensors have column-parallel converters: multiple columns convert signals concurrently rather than sending everything through one distant converter. This connects the camera to the computer lesson: parallel work, timing, signal noise and bandwidth all affect the design. [Sony Semiconductor Solutions: column-parallel conversion](https://www.sony-semicon.com/en/technology/is/columnad.html).

![Invented photodiode charge readout and ADC calculation giving code two hundred fifty, plus a four-by-four Bayer filter mosaic and conceptual demosaicing of single filtered measurements into RGB components.](https://damjan-popic.github.io/assets/images/agrft/v2/camera-sensor.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/camera-sensor.svg)

**A complete numerical model.** Consider an invented photosite and readout chain. These values explain the stages; they are not specifications for a production camera.

1. Light reaching the detector produces a mean of 5,000 incident photons during one exposure.
2. At an assumed quantum efficiency of 0.5, the mean detected charge is 2,500 electrons.
3. Assume the readout chain, after removal of its reference offset, produces 100 μV per electron. The expected signal is therefore 250,000 μV = 0.250 V.
4. An ideal 10-bit ADC spans 0 to 1.024 V in 1,024 equal bins. One bin is 0.001 V. For this model, code = floor(voltage / 0.001 V), limited to 0–1,023.
5. A signal of 0.250 V receives code 250. In ten binary digits this is **0011111010**: 128 + 64 + 32 + 16 + 8 + 2.

The stored code is a measurement label. It is not a photograph of 250 electrons, and it is not the actual number of photons. A neighbouring voltage in the same quantization bin receives the same code. A voltage beyond the converter's range saturates at an end code.

The photon number also fluctuates. In a simple photon-limited model, a mean detected signal of 2,500 electrons has shot-noise standard deviation √2,500 = 50 electrons. In our invented readout chain, that corresponds to 5 mV, or approximately five ADC codes. More output bits would make the numerical steps finer; they would not remove that fluctuation. Real systems additionally have read noise, dark signal and other non-ideal behaviour.

**Full-well capacity** is the charge capacity before a photosite or relevant signal stage saturates. **Read noise** is uncertainty introduced by measuring the charge. **Dark current** produces signal even without incoming scene light and depends on conditions including temperature and integration time. These quantities help define usable dynamic range. For a simplified linear sensor model, a full-well/read-noise ratio of 32,768 corresponds to log2(32,768) = 15 stops. A manufacturer's reported range also depends on the measurement method and the accepted noise threshold. [Hamamatsu: signal-to-noise calculations](https://camera.hamamatsu.com/us/en/learn/technical_information/thechnical_guide/calculating_snr.html), [ARRI: dynamic-range measurement](https://www.arri.com/resource/blob/295460/e10ff8a5b3abf26c33f8754379b57442/2022-09-28-arri-dynamic-range-whitepaper-data.pdf).

A useful consequence follows. Collecting four times as many photons increases photon-limited signal-to-noise ratio by two, because the signal grows by four while its shot-noise standard deviation grows by two. Multiplying a recorded value by four in software multiplies its existing noise as well. Additional measurement precision and additional light solve different problems.

### How a sensor measures colour

Silicon's response is not equivalent to human colour vision. A conventional Bayer sensor places colour filters over photosites: a repeating block contains two green-filtered sites, one red-filtered site and one blue-filtered site. “Red” names a spectral sensitivity band, not a detector that accepts one perfectly pure wavelength.

Each site supplies one filtered measurement. **Demosaicing**, also called debayering for a Bayer pattern, estimates the missing colour components at output locations from neighbouring measurements. The resulting RGB image has several channels per output pixel, but those channels were not all directly measured at each Bayer photosite. Spatial detail and colour detail therefore interact. [Nikon MicroscopyU: colour-filter arrays](https://www.microscopyu.com/digital-imaging/color-balance-in-digital-imaging).

Imagine adjacent measurements R = 700, G = 500, G = 520 and B = 300. They are four spatial measurements under different filters, not four complete RGB pixels. A simple teaching interpolation might average the two green readings to obtain 510 for a local estimate. A real demosaicer uses a larger neighbourhood, edge information and a specified algorithm. Our average cannot reconstruct information never measured, and it cannot identify a real scene colour without calibration.

A sensor's **photosite count**, its resolved detail, and the final file's pixel dimensions are different properties. Fine repeating fabrics can exceed what the optical and sampling system can represent faithfully, producing **aliasing**, false colour or **moiré**. Cropping, binning, line skipping, full-sensor readout and downsampling are different ways to produce a recording mode; the mode's output dimensions alone do not disclose which method was used.

A monochrome sensor may omit the colour-filter array. Other cameras use different filter patterns or separate sensors with a colour-separating prism. Therefore, neither Bayer sampling nor demosaicing is a compulsory stage in every camera. Sony's own documentation includes alternative pixel arrangements, illustrating why “one pixel equals one red, green and blue measurement” is unsafe shorthand. [Sony: Quad Bayer sensor structure](https://www.sony-semicon.com/files/62/pdf/p-13_IMX299CJK_Flyer.pdf), [Nikon MicroscopyU: digital-imaging fundamentals](https://www.microscopyu.com/digital-imaging/fundamentals-of-digital-imaging).

### Exposure time, frame rate and shutter behaviour

**Frame rate** says how many frames are captured or presented per second. **Exposure time** says how long a photosite integrates light for a particular frame. **Readout timing** says when measurements from different locations are transferred or sampled. None is a substitute for the other two.

At 25 frames per second, one frame period is 1/25 s = 40 ms. A 20 ms exposure uses half that period. Camera menus may describe this as 1/50 s or as a **180° shutter angle**. The conventional relationship is:

**exposure time = shutter angle / (360 × capture frame rate).**

The angle terminology comes from rotary shutters in film cameras. On an electronic camera it can describe the equivalent exposure fraction without a rotating disc being present. At 25 fps, 90° gives 10 ms = 1/100 s; 180° gives 20 ms = 1/50 s. At 50 fps, 180° also gives 10 ms. Use the capture rate in this calculation, not the rate to which footage will later be conformed.

A shorter exposure reduces the distance a moving image travels during the measurement, giving less motion blur. It also collects less light under unchanged conditions. A longer exposure gathers more light and spreads a moving subject over more positions. Neither setting changes the number of temporal samples if frame rate stays fixed. A fast shutter at 25 fps can show sharply defined moving positions separated by noticeable temporal jumps.

A **mechanical shutter** blocks light physically. An **electronic shutter** controls integration and readout electronically. A focal-plane mechanical shutter may expose different parts of the frame at slightly different times, especially when a moving slit traverses the image. “Mechanical” does not itself guarantee simultaneous exposure across the whole frame.

![Two timing panels on a common zero-to-forty-millisecond scale: simultaneous twenty-millisecond global exposure for four example rows, and rolling row exposures starting at zero four eight twelve milliseconds and ending twenty milliseconds later.](https://damjan-popic.github.io/assets/images/agrft/v2/camera-shutter.svg)

[Open schematic at full size](https://damjan-popic.github.io/assets/images/agrft/v2/camera-shutter.svg)

In the diagram, four illustrative rows represent positions across a sensor. Each integrates for 20 ms. In the global example, all begin at 0 ms and end at 20 ms. In the rolling example, the starts are 0, 4, 8 and 12 ms; the corresponding ends are 20, 24, 28 and 32 ms. The first-to-last exposure-start skew is 12 ms. The exposure duration of each row remains 20 ms.

**Rolling shutter** means that different rows or regions represent different time intervals. Camera motion or subject motion during the scan can make straight vertical features lean or make rapidly rotating objects distort. **Global shutter** gives all image locations the same exposure interval; the stored measurements may still be read out sequentially afterwards. Global exposure is not synonymous with instantaneous exposure. Motion blur can occur within the shared interval. [Basler: electronic shutter types](https://docs.baslerweb.com/electronic-shutter-types).

CMOS describes sensor technology, not this timing choice. RED's KOMODO documentation provides a concrete example of a CMOS sensor with a global shutter. A specification for maximum frame rate also does not, by itself, state the rolling scan time in every recording mode. [RED: KOMODO technical specifications](https://docs.red.com/955-0196/955-0196_V1.7%20Rev-B%20RED%20PS%2C%20KOMODO%20Operation%20Guide%20HTML/Content/A_TechSpecs/Specs_KOMODO_6K.htm).

**Artificial-light flicker.** A lamp or display can change brightness during the camera's sampling cycle. Different rows may then receive different amounts of light, producing bands; successive frames may vary in brightness. In a 50 Hz mains region, 1/50 s or 1/100 s is a useful starting point for certain lighting, but LED drivers and displays can operate at other frequencies. Test the actual source at its intended dimmer setting and the actual camera mode. Fine shutter adjustment can help, but “180° always prevents flicker” is false. [Sony: reducing camera flicker](https://www.sony.com/electronics/support/cameras-camcorders-camcorders-and-video-cameras/articles/00122281).

### ISO, gain and exposure index

Changing aperture, exposure time, ND or scene illumination can change the number of photons collected. Changing an ISO or EI setting does not inherently make extra photons arrive. What the setting changes depends on the camera and mode.

**Analogue gain** changes the electrical scaling before conversion at a particular stage. **Digital gain** multiplies numerical values after conversion. **Conversion gain** concerns how collected charge becomes a voltage; a sensor may have different conversion-gain modes. The terms describe different operations, even when the camera presents them through a single ISO control.

Additional analogue gain can make a weak signal occupy more ADC codes and can change the contribution of later-stage noise. It cannot restore clipped charge or eliminate photon shot noise. Digital multiplication can brighten the image but multiplies the noise already recorded. Clipping may occur at the photosite, analogue circuitry, ADC or later processing stage; those locations have different consequences.

A camera advertised with two base or “native” ISO settings may offer two useful sensor/readout operating regimes. That does not mean every higher ISO value is another independent physical sensitivity. It also differs from an architecture that reads and combines two gain paths for a single exposure. Describe the documented mechanism rather than equating every label containing “dual.” [Sony: CineAlta workflow guide](https://pro.sony/s3/2024/11/30080042/CineAlta-Workflow-Guide_v1.1.pdf), [ARRI: sensor and processing architecture](https://www.arri.com/en/learn/arri-camera-technology/best-overall-image-quality).

An **exposure index**, or EI, can be used to rate a camera for exposure and monitoring while leaving the chosen base recording mode unchanged. Sony's Cine EI documentation is a specific example. If lowering EI makes the monitoring image appear darker and the operator then opens the lens to restore its appearance, the recorded exposure increases because the operator admitted more light. The EI number did not manufacture that light. Other modes can behave differently, so identify the mode before explaining an ISO change. [Sony: Cine EI](https://helpguide.sony.net/di/pp/v1/en/contents/TP1000756717.html), [Sony: using exposure index](https://helpguide.sony.net/di/pp/v1/en/contents/TP1000756720.html).

**Worked comparison.** Two exposures use the same sensor mode. The first collects a mean of 100 electrons at a dark feature. The second collects 400. Ignoring other noise, their shot-noise standard deviations are 10 and 20 electrons; their signal-to-noise ratios are 10 and 20. Increasing the first image's digital gain by four produces mean 400 and noise 40 in the same scaled units. Its signal-to-noise ratio remains 10. Raising the numerical brightness is not equivalent to recording four times the light.

Exposure decisions also protect highlights. If the desired bright detail has already saturated a relevant capture channel, lowering the image in post-production cannot recover the missing variation. Some software can estimate or reconstruct a plausible highlight from remaining channels; that is not the same as having measured the original detail.

### From sensor values to a recorded picture

The camera's **image-processing pipeline** turns sensor measurements into usable representations. The following table separates functions so that we can name them accurately. Implementations can combine, reorder or distribute them between the camera and later software. Some operations are optional.

| Operation | What changes | What to ask |
|---|---|---|
| Black-level and sensor calibration | Adjusts reference offsets or known sensor behaviour. | Which corrections are applied, and which are described in metadata? |
| Defective-pixel correction | Replaces or estimates values at identified faulty sites. | Is this already applied to the recording? |
| Gain and normalization | Scales the signal or numerical values. | Is the change analogue, digital, or a decode instruction? |
| White-balance processing | Adjusts relative channel responses for the chosen neutral reference. | Is it recorded into the image or retained as adjustable raw metadata? |
| Demosaicing | Reconstructs colour components from a mosaic sensor's measurements. | Which sensor pattern and algorithm are used? |
| Colour transformation | Maps camera responses into a defined working colour representation. | Which input transform and colour space are required? |
| Tone or transfer encoding | Maps signal levels into a defined encoding, including a log curve where selected. | Which exact transfer function describes the values? |
| Spatial processing | Can resize, sharpen, reduce noise or correct lens effects. | Which operations are irreversible in this recording? |
| Chroma subsampling and quantization | May reduce colour sampling and establish stored code precision. | Is the output RGB, 4:4:4, 4:2:2 or another representation, at what bit depth? |
| Compression and file writing | Encodes picture data and stores it with audio, timing and other metadata. | Which codec, container and recording mode are used? |

The processing description must remain attached to the data. The same numbers interpreted through a wrong transfer function or colour transform produce a wrong image. Adobe's DNG specification provides a concrete example of a format carrying black-level, colour-calibration and other interpretation information; ARRI describes the processing needed to turn its sensor data into images. [Adobe: Digital Negative specification and resources](https://helpx.adobe.com/camera-raw/desktop/dng-and-file-formats/digital-negative.html), [ARRI: ARRIRAW FAQ](https://www.arri.com/en/learn/camera-systems/pre-postproduction/file-formats-data-handling/arriraw-faq).

**White balance** chooses how an intended neutral reference should be rendered. Under a simplified linear model, a neutral patch measured as R = 400, G = 800, B = 200 can be normalized using channel multipliers 2, 1 and 4, producing 800, 800, 800. This is a teaching model, not a complete camera colour transform. If the blue measurement is noisy, multiplying it by four also scales that noise.

A colour-temperature setting is expressed in kelvins, such as 3,200 K or 5,600 K. A tint adjustment addresses a different component of the colour balance. A single correction cannot necessarily neutralize subjects lit by several spectrally different sources. Two lamps with the same nominal colour temperature can render coloured objects differently.

In processed video, the chosen white balance and other transformations may already affect recorded values. In many raw workflows they can be changed during decoding because the file preserves appropriate sensor information and metadata. That flexibility does not recover a capture channel that has already clipped. A recorded grey reference and a clear camera report help the colourist distinguish the scene's light from an unintended setting. [Adobe: raw conversion and adjustable camera parameters](https://helpx.adobe.com/camera-raw/desktop/dng-and-file-formats/adobe-dng-converter.html).

**Raw** describes a family of recording approaches retaining sensor-related information for later interpretation. It is not a guarantee of an untouched electrical dump. Raw data can be calibrated, mapped nonlinearly, packed, compressed or partially processed. The exact format matters. Blackmagic RAW, for example, explicitly performs part of demosaicing in the camera. That documented design is enough to disprove “raw always means no demosaicing or processing.” [Blackmagic Design: Blackmagic RAW](https://www.blackmagicdesign.com/products/blackmagicraw).

**Log** describes a transfer encoding that allocates code values differently from a linear representation, commonly to carry a wide exposure range efficiently. It does not say whether the data is raw, which codec stores it, or whether it has been compressed losslessly. A camera can record processed log video. A raw format can also use a nonlinear encoding for its sensor values.

Log material usually needs an appropriate viewing transform to appear as intended on a conventional display. A **LUT**, or lookup table, maps input values to output values. A monitoring LUT can affect only the viewing path or can be applied to a recorded output, depending on configuration. “The LUT is on” is incomplete: ask **which LUT, on which output, and whether it is recorded**. ARRI's documentation distinguishes log encodings, colour spaces and look-file handling. [ARRI: colour FAQ](https://www.arri.com/en/learn/camera-systems/image-science/color-faq), [ARRI: look files](https://www.arri.com/en/learn/camera-systems/image-science/look-files).

Bit depth counts available code combinations. Dynamic range describes a ratio between useful signal extremes under specified conditions. An N-bit linear representation has 2^N possible codes, but an N-bit file does not automatically contain N stops of useful picture range. Noise, clipping, nonlinear encoding and the measurement criterion all intervene. Likewise, a “4K” file specifies neither dynamic range nor colour accuracy.

### Monitoring, stabilization and diagnosing a problem

The monitoring image is one view of the capture pipeline. Its brightness depends on the display and viewing transform. Assessing exposure by turning the monitor brighter is equivalent to changing the playback volume when checking microphone gain: it changes the presentation, not the recorded measurement.

A **waveform monitor** plots image signal levels against horizontal position. A **histogram** counts how values are distributed but does not tell you where each value occurs in the frame. **Zebras** mark a configured level or range. **False colour** maps selected ranges to visible colours. Their meanings depend on the measured signal, scale and camera configuration: a waveform after a LUT is not necessarily showing the same encoding as the recorded log signal. **Focus peaking** highlights selected high-frequency edges; it is an aid, not proof that the intended subject is critically focused. [Blackmagic Design: scopes](https://www.blackmagicdesign.com/ca/products/davinciresolve/color), [camera monitoring tools](https://www.blackmagicdesign.com/sg/products/blackmagiccamera/techspecs).

Image stabilization addresses camera movement. Optical systems move a lens group or sensor to compensate for measured shake. Electronic stabilization modifies the image, often using a crop and geometric corrections. A tripod or gimbal changes the camera's mechanical support and movement. These methods can be combined, but they are not interchangeable. Stabilization does not generally freeze a subject moving independently within the shot. [Nikon: image-stabilization principles](https://www.nikon.com/company/technology/technology_fields/software_and_systems/image_stabilization/).

Describe an observed fault before naming its cause:

| Observation | Plausible investigation |
|---|---|
| Static lettering is soft, while another distance is sharper. | Check focus distance, lens calibration and viewing magnification. |
| Moving hands leave a trail but the background remains sharp. | Check exposure duration and subject movement. |
| Vertical lines lean during a pan. | Check rolling-shutter timing and the camera movement. |
| Bands change when a lamp is dimmed. | Test the source's modulation and the camera's exposure timing. |
| Fine fabric develops coloured patterns. | Investigate optical/sensor aliasing and scaling. |
| Highlights remain flat after lowering exposure in post. | Check which capture or processing stage clipped. |
| The recorded image differs from the on-set monitor. | Check output routing, LUTs, colour management and display configuration. |
| Recording stops although the card still has free space. | Check sustained write performance, media compatibility, temperature and error messages. |

A useful report states the conditions: “The bands appear at 1/100 s when the LED is dimmed below half output. They disappear at full output in the same camera mode.” That gives someone a reproducible observation. “The camera is bad in low light” does not.

### One shot, followed all the way to the edit

Consider an original classroom setup: a locked-off, twenty-second shot of a speaker at a desk. The camera will record **3,840 × 2,160, progressive, 25 fps**. We want natural-looking hand movement, steady colour and enough focus tolerance for small movements. These are proposed conditions for reasoning, not compulsory settings for every production.

First, establish the viewpoint and framing. Choose a lens that covers the active sensor region. Secure the lens and support; find the sensor-plane mark and measure a focus distance if needed. Select an aperture that gives suitable focus tolerance, then assess whether the light level requires ND, additional lighting or a different operating choice. Set 180° as the initial shutter angle, which gives 1/50 s at 25 fps, and test the actual lights for flicker.

Set the sensor/gain mode and a deliberate white balance. Choose the recording representation and monitoring transform. Check focus at a useful magnification and inspect the bright areas through the appropriate exposure tools. Confirm whether the monitor is showing the recording's encoding or a transformed view.

Route audio at the correct input level and monitor it through headphones. If separate sound is recorded, arrange the actual synchronization method and a clear take identifier. Timecode labels aid matching; they do not automatically make all device sample clocks identical. The sound and computer chapters explain why timing, file metadata and media handling remain relevant.

For a storage exercise, suppose the video payload has a constant rate of **200 Mbit/s** and the camera also writes two uncompressed 48 kHz, 24-bit audio channels. In twenty seconds:

- Video payload: 200,000,000 × 20 / 8 = 500,000,000 bytes.
- Audio payload: 48,000 × 24 × 2 × 20 / 8 = 5,760,000 bytes.
- Combined payload: 505,760,000 bytes, approximately 505.76 MB using decimal units.
- Captured frames: 25 × 20 = 500.

The calculation excludes container overhead, additional metadata and any extra recordings. A real variable-rate codec will not necessarily produce exactly this file size. Recording-card capacity and sustained write performance are separate checks.

After the take, confirm that the recording exists and plays correctly. The media workflow preserves the source files, copies the complete required directory structure, verifies the copies and keeps the agreed backups before reuse. The editor receives the image and sound with enough information to interpret them: frame rate, recording mode, camera and reel identifiers, colour space/transfer function, any monitoring look and useful camera notes.

The director of photography determines the photographic approach with the director; camera assistants support the camera and focus work; the DIT contributes technical image and workflow expertise where the production has that role; the sound team records and documents the sound. Responsibilities depend on the production's staffing. The next part of the course names those responsibilities in detail. Here the equipment gives the language a physical meaning.

### The language of a precise explanation

A technical explanation should connect a part to its operation and a decision to its consequence.

| Communicative purpose | Model sentence |
|---|---|
| Identify and locate | “The sensor sits behind the lens mount at the image plane.” |
| Define | “The iris is the mechanism that changes the aperture.” |
| Explain a transformation | “The ADC converts the measured voltage into a numerical code.” |
| State a condition | “At 25 fps, a 180-degree shutter corresponds to 1/50 of a second.” |
| Make a controlled comparison | “With focus distance and focal length unchanged, stopping down increases depth of field under the same sharpness criterion.” |
| Separate observation and inference | “The vertical lines lean during the pan; rolling-shutter timing is one possible cause.” |
| Report a setting | “We recorded log video and used the LUT for monitoring only.” |
| Explain a limit | “The channel was clipped during capture, so lowering the decoded value cannot restore its original variation.” |
| Request the missing specification | “Which active sensor area does this recording mode use?” |
| Describe a change | “We opened the lens by two stops and added two stops of ND.” |

Use **increase the f-number** or **close down the aperture** when that is what you mean. “Increase the aperture” conventionally means make the opening larger, which reduces the f-number. Say **shorter exposure time** when clarity matters; “higher shutter” is ambiguous. Distinguish **capture frame rate** from **playback frame rate**, **sensor** from **processor**, **image** from **file**, and **focus** from **zoom**.

| English term | Slovene orientation |
|---|---|
| focal length | goriščna razdalja |
| angle / field of view | zorni kot / vidno polje |
| entrance pupil | vstopna zenica |
| aperture / iris | zaslonska odprtina / zaslonski mehanizem |
| f-number / T-stop | zaslonsko število / zaslonska vrednost z upoštevanjem prepustnosti |
| transmission / attenuation | prepustnost / slabljenje |
| optical density | optična gostota |
| depth of field / depth of focus | globinska ostrina / toleranca položaja slikovne ravnine |
| photodiode / photosite | fotodioda / svetlobno občutljivo mesto na tipalu |
| charge / voltage / gain | električni naboj / napetost / ojačenje |
| quantum efficiency | kvantni izkoristek |
| integration / exposure time | integracijski / osvetlitveni čas |
| readout / read noise | odčitavanje / šum odčitavanja |
| full-well capacity | največja količina naboja pred nasičenjem |
| colour-filter array / demosaicing | matrika barvnih filtrov / rekonstrukcija barv iz mozaičnih meritev |
| rolling / global shutter | časovno zamaknjena osvetlitev vrstic / sočasna osvetlitev vseh svetlobno občutljivih mest |
| white balance / colour temperature | nastavitev beline / barvna temperatura |
| highlight clipping / headroom | odrez svetlih vrednosti / razpoložljiva rezerva |
| monitoring LUT / recorded look | pregledovalna preslikava LUT / v zapis vključena podoba |
| codec / container / metadata | kodirnik-dekodirnik / vsebnik / metapodatki |

The Slovene column supplies orientation, not a claim that every workplace uses one fixed equivalent. In English, use the term that identifies the actual mechanism. An accurate explanation can be short: “This control changes the exposure index in the monitoring workflow; it does not change the selected base sensor mode.” That sentence is more useful than a long description built around an unidentified “quality” setting.

## 5. People, professions and terminology

Professional vocabulary makes responsibilities and decisions precise. Saying that you *edit dialogue scenes, organise rushes, or pull focus* identifies a contribution. Learn terms with their usual verbs: a director **blocks a scene**, a camera assistant **pulls focus**, an editor **assembles a sequence**, and a colourist **matches shots**.

Directing, cinematography and editing also require neighbouring departments' vocabulary: an editor must understand a sound request; a director must distinguish a performance problem from a production constraint.

The Slovene column offers established equivalents or functional descriptions. Job boundaries differ between countries and productions. A small documentary may combine responsibilities that a large drama separates among specialists. Ask what someone is responsible for before relying on a title alone. ScreenSkills' departmental checklists recognise variation in scale, budget and genre; its profiles mainly describe British practice.

Ceramella and Lee introduce television, camera and editing language on pp. 42–51 and film roles on p. 52 of *Cambridge English for the Media* (2008). Their terminology provides a useful starting point. The distinctions below also draw on current professional role descriptions and technical documentation. All worked situations in this chapter are original examples.

### The basic units of screen work

Precision matters when identifying material, planning coverage or explaining an edit.

| English term | Meaning and professional use | Slovene orientation |
| --- | --- | --- |
| **frame** | One image in moving-image material; also the visible boundary within which elements are composed. | posamezna sličica; slikovni okvir |
| **shot** | An uninterrupted image passage in the finished work; during production, also a planned camera view or recording setup. | kader |
| **take** | One recorded attempt at a shot or performance: *take three of the doorway close-up*. | posamezna ponovitev snemanja kadra |
| **scene** | A dramatic unit, commonly organised around a particular place and time; it may contain many shots. | prizor |
| **sequence** | A connected passage of action that may contain several scenes; in editing software, also a particular timeline assembly. | sekvenca; v programu tudi montažno zaporedje |
| **setup** | A particular arrangement of camera, lighting and other relevant equipment for recording. | snemalna postavitev |
| **coverage** | The range of views and performances recorded to give the editor material for constructing a scene. | posneti kadri, potrebni za sestavo prizora |
| **footage** | Recorded moving-image material, whether or not it appears in the finished work; usually uncountable. | posneto filmsko oziroma videogradivo |
| **cast** | The performers engaged for a production; a collective noun, distinct from the crew. | igralska zasedba |
| **crew** | The people doing the production's technical, creative and organisational work behind the performance. | filmska oziroma televizijska ekipa |

A scene in a kitchen might contain a wide shot and two close-ups. Each camera view might be recorded four times. Those recordings are **takes**, although the editor may use only part of one take in the finished **shot**. A **long take** concerns duration; a **long shot** concerns how widely the subject is framed. A three-second long shot is perfectly possible.

An editor saying “open the sequence” probably means a timeline; a critic discussing “the escape sequence” means a narrative passage. Neither necessarily corresponds to one numbered screenplay scene.

Use *some footage*, *three clips*, or *five shots*. Avoid *three footages*. A **clip** is a media item or a portion used in an edit; one recorded take can supply several clips or several uses of the same clip. These distinctions extend the camera and editing vocabulary in Ceramella and Lee (2008, pp. 48–52).

### Directing, performance and continuity

The director connects story, performance and audiovisual form. Assistant directing makes the filming plan workable; script supervision records information needed for coherence across takes and in the edit.

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **director** | Develops the creative interpretation and directs performances and staging, working with the producer, cinematographer and editor. | režiser, režiserka |
| **screenwriter** | Writes and revises the screenplay, developing action, characters and dialogue with the relevant creative decision-makers. | scenarist, scenaristka |
| **actor** | Interprets and performs a character, working with the director and other performers. *Actor* can refer to any gender. | igralec, igralka |
| **performer** | A broader term covering people whose performance is filmed, including actors, dancers and other performance specialists. | nastopajoča oseba; izvajalec, izvajalka |
| **first assistant director / 1st AD** | Coordinates the practical shooting operation and schedule, communicating between the director and departments. | prvi asistent režije; organizacija snemanja |
| **second assistant director / 2nd AD** | Supports the 1st AD through cast arrangements, call-sheet information and readiness away from the immediate shooting floor. | drugi asistent režije |
| **script supervisor** | Tracks coverage, continuity, script changes and take information, supplying useful records to directing and editorial teams. | skrb za kontinuiteto in zapis poteka snemanja |
| **blocking** | The planned positions and movements of performers in relation to one another, the space and the camera. | določitev postavitev in gibanja nastopajočih |
| **rehearsal** | A preparation run used to work through performance, movement or technical coordination before the recorded take. | vaja |
| **mark** | A specified position a performer or piece of equipment should reach; often physically indicated. | označeno mesto oziroma pozicija |
| **eyeline** | The direction of a person's gaze, which must communicate the intended spatial relationship across shots. | smer pogleda |
| **continuity** | Consistency needed for the intended connection between shots: action, appearance, objects, space, sound and other details. | kontinuiteta |
| **axis of action / line of action** | An imagined spatial reference used to maintain or deliberately change the viewer's orientation across views. | os dogajanja |
| **script breakdown** | Analysis of the script into production requirements such as cast, locations, props and special needs. | razčlenitev scenarija za pripravo produkcije |
| **shooting script** | The script version used to organise production, normally with numbered scenes and controlled revisions. | snemalni scenarij; izvedbena različica scenarija |
| **sides** | The selected script pages needed for a particular day's work or audition. | izbrane strani scenarija |

The first AD is not simply the director's personal assistant or an apprentice doing a little directing. Compare: “The director wants the pause to feel uncomfortable” and “The first AD needs to know whether we require another setup.” The first concerns creative effect; the second concerns the practical consequences of achieving it. A director may change a performance; the script supervisor records what changed and its implications for continuity.

**Blocking** does not mean obstructing something here. “We changed the blocking so that she reaches the window before the line” describes coordinated action. A useful continuity note identifies the event: “In take two, he puts the cup down before answering; in take four, he is still holding it.” The note gives the editor a specific relationship to assess.

Professional sources: ScreenSkills, [Director](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/development-film-and-tv-drama-job-profiles/director-film-and-tv-drama/), [Screenwriter](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/development-film-and-tv-drama-job-profiles/screenwriter-film-and-tv-drama/), [Assistant director](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/production-management/assistant-director/), [Second AD skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/assistant-directors-department/key-second-assistant-director-key-2nd-ad-skills/) and [Script supervisor skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/script-supervisor-department/script-supervisor-skills/).

### Cinematography and the camera department

**Cinematography** includes the decisions through which light, lenses, exposure, framing and movement produce the image. Operating the camera is one part of that work. The cinematographer may operate on some productions, but *cinematographer* and *camera operator* are not automatically equivalent credits.

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **director of photography / DoP / DP / cinematographer** | Leads the photographic approach with the director and coordinates its implementation with camera, lighting and grip specialists. | direktor fotografije; oblikovanje filmske podobe |
| **camera operator** | Frames and operates the camera during the shot, coordinating movement with performers, camera assistants and grips. | operater kamere |
| **first assistant camera / 1st AC / focus puller** | Maintains accurate focus and supports camera preparation and technical operation with the operator and camera team. | prvi asistent kamere; ostrilec |
| **second assistant camera / 2nd AC** | Handles slating, records and camera support; media responsibilities depend on the production's agreed workflow. | drugi asistent kamere; klapa in podpora kameri |
| **digital imaging technician / DIT** | Supports the DoP's digital image workflow, including image monitoring, settings and agreed colour-management procedures. | tehnik digitalne slike |
| **data wrangler** | Carries out the assigned media offload, verification, organisation and backup procedure, coordinating with camera and post-production. | oseba, odgovorna za prevzem in varovanje podatkov |
| **video assist operator** | Provides monitored and recorded playback for the director and other authorised users; coordinates with camera and production. | operater sistema za videoasistenco in predvajanje |

A DIT should not be described simply as “the person who copies the cards”. Imaging decisions and data handling are related, but the same crew member does not necessarily own both functions. Ask who checks copies, who authorises card reuse, and who passes the material and reports to editorial. Similarly, playback at the director's monitor and the camera's original recording are different things.

Sources: ScreenSkills, [Director of photography](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/director-of-photography-dop/), [Camera operator skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/camera-department/camera-operator-skills/), [First AC skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/camera-department/first-assistant-camera-technicianfocus-puller-skills/), [Second AC skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/camera-department/second-assistant-camera-technicianclapper-loader-skills/), [DIT](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/digital-imaging-technician-film-and-tv-drama/), [Data wrangler](https://www.screenskills.com/job-profiles/browse/unscripted-tv/technical/data-wrangler/) and [Video assist operator](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/video-assist-operator/).

#### Describing the image

| English term | Meaning and use | Slovene orientation |
| --- | --- | --- |
| **wide shot / long shot** | Shows the subject within substantial surrounding space; a framing category rather than a particular lens. | širok plan z okolico |
| **medium shot** | Frames a person at approximately waist level upwards; exact boundaries depend on the production's terminology. | približno srednji plan |
| **close-up / CU** | Isolates a face or important detail in a tight framing; specify what the image includes. | tesen izrez obraza ali podrobnosti |
| **over-the-shoulder shot / OTS** | Frames one person past part of another person's shoulder or head. | kader čez ramo |
| **point-of-view shot / POV** | Represents what a character sees from their implied viewing position. | subjektivni kader |
| **master shot** | Records the main action of a scene in a sustained view that can support the scene's overall construction. | nosilni kader celotnega dogajanja prizora |
| **insert** | A shot emphasising a particular detail within the action, such as a hand changing a setting. | vmesni kader podrobnosti; insert |
| **cutaway** | A shot moving attention away from the principal action to related material. | vmesni oziroma odmikajoči kader |
| **pan** | Rotates the camera horizontally from its position. | vodoravni zasuk kamere |
| **tilt** | Rotates the camera vertically from its position. | navpični zasuk kamere |
| **tracking shot** | Moves the camera through space, often following or accompanying action. | vožnja oziroma premik kamere skozi prostor |
| **dolly** | A camera-support platform used for controlled movement; *dolly in* means move the camera closer. | voziček za kamero; vožnja kamere |
| **zoom** | Changes focal length while the camera may remain stationary, changing the field of view. | sprememba goriščnice; zum |
| **handheld** | Describes a camera held and supported by the operator rather than a fixed support. | snemanje s kamero iz roke |

“Move in” is ambiguous. It might mean a physical camera move, a lens change, a zoom, or tighter framing in the edit. Specify the operation: “Dolly towards her while maintaining the eyeline,” “Zoom in slowly,” or “Crop the shot more tightly in the edit.” A physical move changes the viewpoint; a zoom from a fixed position does not create that same change in perspective.

A **wide shot** describes framing; a **wide-angle lens** describes field of view for a given image format. A **master shot** covers action; an **establishing shot** establishes place or spatial relationships. One shot may serve both functions.

Sources: Ceramella and Lee (2008, pp. 48–51); Adobe, [Pan shots](https://www.adobe.com/uk/creativecloud/video/production/cinematography/camera-shots-and-angles/pan-shot.html), [Master shots](https://www.adobe.com/creativecloud/video/production/cinematography/camera-shots-and-angles/master-shot.html) and [Dolly zoom](https://www.adobe.com/creativecloud/video/production/cinematography/camera-shots-and-angles/dolly-zoom-shot.html).

#### Describing capture settings

| English term | Meaning and use | Slovene orientation |
| --- | --- | --- |
| **focal length** | A lens property, expressed in millimetres, affecting field of view together with the image format. | goriščna razdalja |
| **depth of field** | The range of distances that appear acceptably sharp under the relevant viewing conditions. | globinska ostrina |
| **aperture / iris** | The aperture is the opening through which light passes; the iris mechanism adjusts its size. *Open up* and *stop down* describe increasing and reducing the opening. | odprtina zaslonke; mehanizem za njeno uravnavanje |
| **stop** | An exposure interval corresponding to twice or half the amount of light. | zaslonska oziroma ekspozicijska stopnja |
| **f-stop / T-stop** | An f-number describes aperture geometrically; a T-number also accounts for the lens's measured light transmission. | geometrijska in transmisijska vrednost zaslonke |
| **shutter speed / shutter angle** | Two ways to describe exposure duration; an angle expresses its proportion of the frame cycle. | čas osvetlitve; kot zaklopa |
| **frame rate / fps** | The number of frames per second; distinguish capture rate from playback or timeline rate. | frekvenca sličic |
| **white balance** | A setting or adjustment establishing how the system interprets neutral colour under the illumination. | nastavitev beline |
| **neutral-density filter / ND filter** | Reduces light entering the camera while aiming to preserve colour balance. | nevtralno sivi filter |
| **focus pull / rack focus** | A deliberate change in focus distance during the shot. | preostritev med snemanjem |
| **aspect ratio** | The proportional width and height of an image, such as 16:9; distinct from pixel dimensions. | razmerje stranic |

“Make it brighter” does not specify whether to change lighting, aperture, exposure time or a later image adjustment. A technical explanation should name both the operation and its consequence: “We opened the aperture, which reduced the depth of field,” or “We kept the aperture and added light.” Avoid treating all brightening operations as interchangeable.

When describing slow motion, report two rates: “We recorded at 50 fps and play the material at 25 fps.” That example implies half-speed playback when each recorded frame is shown once. Merely saying “50 fps” does not establish whether the final presentation is slow motion.

Sources: Nikon, [Understanding maximum aperture](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/understanding-maximum-aperture) and [A basic look at exposure](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/a-basic-look-at-the-basics-of-exposure); Canon, [Iris](https://www.canon.com.au/get-inspired/glossary/iris); ZEISS, [Zoom or prime lens?](https://lenspire.zeiss.com/photo/en/article/3-zoom-or-prime-lens-a-shootout-comparison/); ARRI, [Electronic and mirror shutter white paper](https://www.arri.com/resource/blob/178016/ad23969317dafff402f0902d47bb4ab7/alexa-studio-electronic-and-mirror-shutter-white-paper-data.pdf); Adobe, [Aspect-ratio preservation](https://helpx.adobe.com/ie/premiere/desktop/edit-projects/intro-to-editing/aspect-ratio-preservation.html).

### Lighting and grip

The cinematographer describes the intended photographic result; lighting and grip specialists implement it within their responsibilities. Department boundaries differ internationally. Establish who handles lighting support, camera support and movement on the particular production.

| English term | Meaning and professional use | Slovene orientation |
| --- | --- | --- |
| **gaffer** | Leads the lighting department and implements lighting plans with the DoP and lighting crew. | vodja osvetljave |
| **best boy electric / assistant chief lighting technician** | The gaffer's principal assistant, commonly coordinating lighting personnel, equipment and departmental logistics. | glavni pomočnik vodje osvetljave |
| **lighting technician / electrician** | Installs, operates and maintains assigned lighting equipment under the department's supervision. | osvetljevalec; električar v ekipi |
| **key grip** | Leads the grip department, planning the appropriate support and movement systems with cinematography and production. | vodja ekipe za podporo in premikanje kamere |
| **dolly grip** | Prepares and operates the camera dolly and related movement, coordinating with operator, focus puller and performers. | operater vozička za kamero |
| **key light** | The principal light shaping the subject in a particular lighting arrangement. | glavna luč |
| **fill light** | Light used to control contrast by illuminating areas otherwise in shadow. | dopolnilna luč |
| **backlight** | Light reaching the subject from behind, often defining an edge or separating it from the background. | zadnja luč; protisvetloba glede na postavitev |
| **practical** | A visible light source belonging to the scene, such as a desk lamp. | svetilo, vidno v prizoru |
| **diffusion** | Material or a process used to spread light and alter its quality. | razprševanje svetlobe; difuzija |
| **bounce** | Light redirected from a reflecting surface; also the surface used for that purpose. | odbita svetloba; odbojna površina |
| **flag** | An opaque light-control panel used to block or limit unwanted light. | zaslon za omejevanje svetlobe |
| **negative fill** | Reduction of unwanted reflected light, often with a dark surface, to increase local contrast. | odvzem odbite svetlobe |

“The light is too harsh” concerns its quality; “the face is overexposed” concerns the recorded result. They may occur together, but one does not define the other. Likewise, **soft light** can be bright, and **hard light** can be dim. Explain the visible problem before proposing the change: “The shadow edge is too sharp; we need a larger apparent source.”

Sources: ScreenSkills, [Gaffer skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/lighting-department/gaffer-skills/), [Best boy electric skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/lighting-department/best-boyassistant-chief-lighting-technician-skills/), [Lighting technician skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/lighting-department/lighting-technician-skills/), [Key grip skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/grips-department/key-grip-skills/) and [Dolly grip skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/grips-department/dolly-grip-camera-grip-skills/); ARRI, [Lighting handbook](https://www.arri.com/resource/blob/127830/409091c612f371b0c68b41d9dcb636db/arri-lighting-handbook-english-data.pdf) and [Hard light](https://www.arri.com/en/lighting/led-panel-lights/skypanel-x/hardlight).

### Producing, production management and locations

Producing, management and coordination involve different responsibilities. **Production** itself can mean the whole project or the shooting stage between pre-production and post-production.

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **producer** | Develops and realises the project, bringing together creative work, resources and production decisions with the director and other partners. | producent, producentka |
| **executive producer** | A senior producing credit that may concern financing, commissioning or overall oversight; its meaning depends on the production. | izvršni producent; preveriti konkretne pristojnosti |
| **line producer** | Plans and controls the production's practical resources and expenditure with production management and department heads. | operativno vodenje produkcije in proračuna |
| **production manager / PM** | Manages everyday production logistics and implementation of plans, usually working closely with the line producer. | vodja produkcije |
| **production coordinator / PC** | Organises production-office information, documents and arrangements under production management. | koordinator produkcije |
| **location manager** | Finds and manages filming locations, coordinating access and practical requirements with production and departments. | vodja lokacij |
| **production assistant / PA / runner** | Provides assigned practical or administrative support; precise duties depend on department and production. | produkcijski asistent; pomoč pri izvedbi |
| **recce / location visit** | An inspection of a potential location; specify whether the visit evaluates creative suitability or technical requirements. | ogled lokacije |
| **call sheet** | The daily document communicating work, timings, locations, personnel and relevant production instructions. | dnevni snemalni načrt oziroma razpored |
| **shooting schedule** | The planned order and timing of filming across production days. | snemalni razpored |
| **call time** | The time a named person or department must report at the specified place. | čas prihoda oziroma nastopa dela |
| **wrap** | Completion of the specified work: a performer, location, day or whole shoot can wrap. | zaključek določenega dela snemanja |
| **deliverable** | An item that must be supplied under agreed requirements, such as a master, subtitle file or publicity text. | zahtevano gradivo za predajo |
| **clearance** | The process or confirmation of obtaining the permissions needed for a specified use of material. | ureditev potrebnih dovoljenj |

An **executive producer** is not reliably identified by translating each word into Slovene and assuming a familiar local hierarchy. A **line producer** is not the person who writes dialogue lines. When describing your own experience, explain scale and responsibility: “I coordinated locations and call sheets for a five-day student shoot” is more informative than an inflated title.

A **location scout** searches for suitable filming locations; **location scouting** names the activity. A **recce** is an inspection visit. For an example of the person's role, see [Screen Tasmania's explanation of location selection](https://www.screen.tas.gov.au/film_in_tasmania/location_submissions_-_faqs/accordion/how_does_being_chosen_as_a_location_work).

A call time is not automatically the time the camera starts recording. “Cast call at 08:00; first shot planned for 09:30” communicates two different milestones. Similarly, “We wrap the location at 18:00” needs practical clarification if clearing equipment and restoring the space must also happen before access ends.

Sources: ScreenSkills, [Producer](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/development-film-and-tv-drama-job-profiles/producer-film-and-tv-drama/), [Executive producer](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/development-film-and-tv-drama-job-profiles/executive-producer-film-and-tv-drama/), [Line producer](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/production-management/line-producer-film-and-tv-drama/), [Production manager](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/production-management/production-manager-film-and-tv-drama/), [Production coordinator](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/production-management/production-coordinator-film-and-tv-drama/) and [Locations manager](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/production-management/locations-manager/).

### Art, costume, make-up and casting

These departments contribute to character, period, place and visual relationships. Their creative and practical decisions affect cinematography and continuity.

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **production designer** | Develops the production's designed physical world with the director and coordinates its realisation with art and other departments. | scenograf; oblikovanje vizualnega sveta produkcije |
| **art director** | Coordinates the practical development and execution of the agreed design, working with the production designer and art team. | izvedbeno vodenje scenografije oziroma likovne zasnove |
| **set decorator** | Selects and arranges furnishings and dressing that establish the space, working with design and props departments. | oprema in dekoracija prizorišča |
| **props master** | Leads the acquisition, preparation, tracking and care of props required by the production. | vodja rekvizitov |
| **costume designer** | Designs characters' clothing in relation to story, period and visual approach, coordinating with directing and other design departments. | kostumograf, kostumografka |
| **hair and make-up designer** | Develops and supervises the performers' hair and make-up look in coordination with costume, production design and directing. | oblikovalec maske in pričeske |
| **casting director** | Finds and evaluates performers for roles, presents options and supports casting decisions with director and producer. | vodja izbora igralske zasedbe |
| **stand-in** | Substitutes for a principal performer during technical preparation, helping camera and lighting reproduce relevant positions. | nadomestna oseba pri tehnični pripravi |
| **extra / background artist / supporting artist** | Performs background action, following the relevant directing instructions; not the same as a stand-in. | statist, statistka |
| **prop** | An object used or handled within the action; boundaries with set dressing depend on departmental arrangements. | rekvizit |

A stand-in helps prepare a shot; a stunt double performs specified action on another performer's behalf; a background artist contributes to the filmed scene. Those descriptions identify different work even if a small production combines assignments. Similarly, an object can be important both as part of the setting and as an item handled in the action. Ask who prepares, tracks and resets it rather than resolving ownership through a dictionary alone.

Sources: ScreenSkills, [Production designer skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/art-department/production-designer-skills/), [Props master skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/props-department/props-master-skills/), [Costume designer skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/costume-department/costume-designer-skills/), [Hair and make-up designer skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/hair-make-up-and-prosthetics-department/hair-and-make-up-designer-skills/) and [Casting director](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/development-film-and-tv-drama-job-profiles/casting-director/); SAG-AFTRA, [Standing up for stand-ins](https://www.sagaftra.org/standing-stand-ins).

### Recording sound on location

A sound report identifies sources, problems and usable alternatives. “The sound is bad” does not distinguish traffic, clothing noise, distortion, an unwanted reflection or an interrupted line.

| English term | Meaning and professional use | Slovene orientation |
| --- | --- | --- |
| **production sound mixer / sound recordist** | Leads or carries out location sound recording, coordinating microphone coverage and usable tracks with directing, camera and performers. | snemalec zvoka; vodja snemanja zvoka |
| **boom operator / first assistant sound** | Positions and operates microphones for the sound mixer while coordinating with camera, lighting and performers. | mikrofonist; prvi asistent zvoka |
| **lavalier / lav** | A small microphone worn on the body or attached to clothing; it may use a wired or wireless connection. | osebni oziroma pripenjalni mikrofon |
| **radio mic / wireless microphone** | A microphone system transmitting its signal wirelessly; the microphone may be body-worn, handheld or another type. | radijski oziroma brezžični mikrofon |
| **boom microphone** | A microphone carried on a boom pole or support; *boom* names the support arrangement. | mikrofon na palici |
| **sync sound** | Sound recorded with, or aligned to, corresponding picture action. | sinhroni zvok |
| **room tone** | The relatively steady sound of the recording space without the intended dialogue or action. | osnovni zvočni značaj prostora |
| **wild track** | Sound recorded separately from a synchronised picture take, such as an additional line or environmental sound. | ločeno posnet zvok |
| **isolated track / ISO track** | A separately recorded microphone or source track retained for later control. | ločena sled posameznega vira |
| **mix track** | A combined recording of selected sources, often serving as a guide alongside isolated tracks. | združena zvočna sled |
| **clipping** | Distortion caused when a signal exceeds a relevant system's representable or usable range. | popačenje zaradi presežene ravni signala |
| **headroom** | The margin available above an operating signal level before overload. | razpoložljiva rezerva do preobremenitve |

A **boom** and a **shotgun microphone** are different categories: one describes support and positioning, the other a highly directional microphone design. A lavalier can be wired or wireless. These distinctions prevent equipment requests such as “a wireless boom” from concealing several separate requirements.

Room tone is not digital silence. It can help maintain a believable acoustic background around edited dialogue. Wild recording describes how material is recorded relative to picture; it does not mean random or unusable sound. “We recorded the closing line wild because a passing vehicle covered the original” explains both purpose and limitation.

Sources: ScreenSkills, [Production sound mixer skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/production-sound-department/production-sound-mixer-skills/) and [First assistant sound skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/production-sound-department/first-assistant-sound-skills/); Shure, [Audio terminology](https://www.shure.com/en-US/insights/helical-and-145-other-audio-terms-you-may-need-to-know) and [Shotgun microphones](https://www.shure.com/en-US/insights/shotgun-mics-and-video-production); Sound Devices, [Scorpio user guide and glossary](https://guides.sounddevices.com/scorpio/).

### Editing and assistant editing

Editing constructs the viewer's experience through selection, order, duration and relationships between picture and sound. Assistant editing establishes the reliable organisation and exchanges on which that work depends. An assistant editor's work is therefore not adequately described as “helping with the software”.

#### People and stages

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **picture editor / editor** | Shapes the audiovisual construction with the director, selecting and arranging material and refining rhythm, information and performance. | montažer, montažerka slike |
| **assistant editor** | Prepares, organises and synchronises media and manages assigned technical exchanges so editorial and finishing teams can work reliably. | asistent montaže |
| **post-production supervisor** | Coordinates post-production schedules, resources and handovers among editorial, sound, colour, VFX and production. | vodja oziroma koordinator postprodukcije |
| **assembly** | An initial organisation of recorded material into a provisional continuous structure. | začetna sestava posnetega gradiva |
| **rough cut** | A developing version in which structure, selections and timing remain open to substantial revision. | groba montaža |
| **fine cut** | A more developed version undergoing detailed refinement; the exact approval status must still be stated. | fina montaža |
| **director's cut** | A version reflecting the director's choices within the production's approval process; not automatically the released version. | režiserjeva različica |
| **picture lock** | An agreed point at which picture selection and timing are fixed for downstream work; later changes require explicit coordination. | potrjena, časovno zaključena montaža slike |
| **offline edit** | The creative editorial stage, often using manageable working media; the term does not mean disconnected from the internet. | ustvarjalna montaža z delovnim gradivom |
| **online edit / finishing** | Technical completion using appropriate-quality material, including conform, graphics, repairs and coordination with colour and delivery. | tehnična finalizacija |
| **conform** | Reconstructing or checking an approved edit against the required source media in a finishing or receiving system. | uskladitev potrjene montaže z izvornim gradivom |

**Editing** is the ordinary English word for *montaža*. English **montage** often identifies a compressed or associative passage, or a particular aesthetic principle. “I study editing” communicates a professional specialism. “I am building a montage of the factory's closing stages” names a particular construction within a work.

Picture lock does not mean that sound, grading, subtitles and credits are complete. It provides an agreed picture reference for those processes. If the director removes twelve frames after sound has begun work, the alteration is a picture change with consequences, even if it looks minor. Name the version and communicate the change; “the final cut” alone is too ambiguous to identify a file.

Sources: ScreenSkills, [Editor](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/post-production/editor-film-and-tv-drama/), [Edit assistant](https://www.screenskills.com/job-profiles/browse/post-production/edit-suite/edit-assistant-post-production/), [Online editor skills](https://www.screenskills.com/skills-checklists/unscripted-tv/post-production-department/online-editor-skills/) and [Post-production supervisor](https://www.screenskills.com/job-profiles/roles/post-production-supervisor/).

#### Media, structure and references

| English term | Meaning and use | Slovene orientation |
| --- | --- | --- |
| **rushes / dailies** | Production recordings prepared for viewing and editorial work; usage may refer to originals or review versions. | dnevno posneto gradivo; delovni posnetki |
| **ingest** | The organised introduction of source material into a working system, potentially including copying, verification and conversion. | organizirani prevzem gradiva |
| **logging** | Recording descriptions and identifiers that make material searchable and understandable. | popisovanje in označevanje gradiva |
| **bin** | An organisational container inside editing software; not necessarily a matching physical folder on disk. | zbirka gradiva v montažnem programu |
| **timeline** | A time-based representation of arranged image, sound and other elements. | časovnica |
| **clip** | A media item or a selected use of media within an editing project. | izsek oziroma programska enota gradiva |
| **sync / synchronise** | Align picture and sound, or multiple recordings, to the same event in time. | časovno uskladiti |
| **proxy** | A substitute working file designed for efficient editing, linked to the appropriate original media. | nadomestna delovna datoteka |
| **transcode** | Convert media into a different encoding; the result may serve editing, delivery or another purpose. | prekodirati |
| **relink** | Restore a project's connection to the correct media files. | ponovno povezati projekt z datotekami |
| **timecode** | A time-based address used to identify positions; its interpretation requires the relevant frame-rate and counting convention. | časovna koda |
| **source / sequence timecode** | Respectively, an address within source media and an address within the assembled edit. | časovna koda vira oziroma montaže |

A proxy is not automatically a backup: it may have reduced information and cannot be assumed to replace the original. Transcoding is a process; proxy is a function a resulting file may serve. Exporting a film is another operation again. These distinctions matter when asking what has actually been delivered.

“At 01:03:12:08” is incomplete unless the recipient knows which version and which timecode you mean. Prefer: “In `Harbour_v03`, sequence timecode 01:03:12:08, the dialogue starts late.” Original file names, clip identifiers and reference versions allow another department to reproduce the observation.

Sources: Adobe, [Ingest and proxy workflows](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html) and [Reconnect full-resolution media](https://helpx.adobe.com/sg/premiere/desktop/organize-media/ingest-proxy-workflow/reconnect-full-resolution-media-to-proxies.html); ScreenSkills, [Editor skills](https://www.screenskills.com/skills-checklists/scripted-film-and-tv/editorial-department/editor-skills/).

#### Explaining an edit precisely

| English term | Meaning and use | Slovene orientation |
| --- | --- | --- |
| **trim** | Adjust a clip boundary to change which part or duration is used. | natančno prilagoditi začetek ali konec izseka |
| **ripple edit** | Changes a boundary and shifts following material on the affected tracks, changing the relevant duration. | rez s premikom nadaljnjega gradiva |
| **rolling edit** | Moves a shared cut between adjacent clips while preserving their combined duration. | premik skupne meje dveh izsekov |
| **slip edit** | Changes the source portion inside a clip while preserving its timeline position and duration. | sprememba vsebine znotraj nespremenjenega izseka |
| **slide edit** | Moves a clip while preserving its content and duration, adjusting neighbouring boundaries. | premik izseka s prilagoditvijo sosednjih mej |
| **J-cut** | The incoming sound begins before its corresponding incoming picture. | predhodni vstop zvoka naslednjega kadra |
| **L-cut** | The outgoing sound continues after the picture has moved to the next shot. | nadaljevanje zvoka čez slikovni rez |
| **match cut** | Connects shots through a meaningful similarity in image, movement or another perceptible feature. | rez na podlagi ujemanja |
| **jump cut** | Creates a noticeable discontinuity, often by removing time within a similar view of the same subject. | skokoviti rez |
| **cut on action** | Places a cut during an action so movement helps connect the two views. | rez na gibanju |
| **handles** | Additional source material before and after a used section, supplied for later adjustment or transitions. | dodatno gradivo pred in za uporabljenim izsekom |
| **turnover** | A defined handover of an edit, media and accompanying information to another post-production department. | predaja gradiva naslednjemu oddelku |

“Make the reaction earlier” could require a slip, a moved cut or a structural change. Specify what must remain constant. “Use an earlier reaction from the same take, keeping the clip's duration and timeline position” describes a slip. “Give the reaction eight more frames without changing the scene's duration” may call for moving a shared cut. The language expresses editorial intent before any software command is chosen.

With split edits, picture and sound boundaries occur at different times. If we hear a train before seeing the station, the incoming sound can create a J-cut. If a departing character's voice continues over the listener, that outgoing sound can create an L-cut. These names describe the relationship, not a guarantee that the transition is appropriate.

Sources: Adobe, [Ripple edits](https://helpx.adobe.com/uk/premiere/desktop/edit-projects/trim-clips/perform-ripple-edits.html), [Rolling edits](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-rolling-edits.html), [Slip edits](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-slip-edits.html), [Slide edits](https://helpx.adobe.com/no/premiere/desktop/edit-projects/trim-clips/perform-slide-edits.html) and [J-cuts and L-cuts](https://helpx.adobe.com/uk/premiere/desktop/edit-projects/trim-clips/perform-j-cuts-and-l-cuts.html).

#### Exchange and delivery

| English term | Meaning and use | Slovene orientation |
| --- | --- | --- |
| **edit decision list / EDL** | A structured list identifying edit events and their source and sequence positions; supported detail depends on the format. | montažni seznam |
| **AAF / XML interchange** | Formats used to exchange project information between applications; media inclusion and supported features must be checked. | formati za izmenjavo montažnih podatkov |
| **render** | Calculate an image or sound result from source material and processing instructions. | izračunati obdelano sliko oziroma zvok |
| **export** | Write a selected result or project representation to an output format. | izvoziti |
| **codec** | A method or implementation for encoding and decoding media. | kodek |
| **container / wrapper** | The file structure holding media streams and associated information, such as an MP4 or MOV file. | vsebnik oziroma datotečni ovoj |
| **master** | An authoritative high-quality output prepared for a defined use or distribution workflow. | končna matična različica |
| **quality control / QC** | Systematic checking of the actual output against its content and technical requirements. | kontrola kakovosti |

“Send an MP4” names a container, not a complete specification. Resolution, frame rate, encoding, audio and the intended use still matter. Equally, a successful export is not proof that the exported file has correct synchronisation, titles or content. A precise handover identifies the output and the reference against which it was checked.

Sources: Adobe, [EDL export](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-project-as-an-edl-file.html) and [Export settings reference](https://helpx.adobe.com/media-encoder/desktop/encoding-and-exporting/export-settings-reference.html); Avid, [AAF format](https://kb.avid.com/pkb/articles/en_US/Knowledge/en336549).

### Sound post-production

The **soundtrack** is the complete sound component of the work, including dialogue, music and effects. A commercial album called a soundtrack may contain only music. For production discussion, distinguish the complete soundtrack from the **score** and from individual sound elements. This is a necessary refinement of the brief vocabulary presentation in Ceramella and Lee (2008, p. 52).

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **supervising sound editor** | Plans and oversees sound editorial work, coordinating specialists, creative decisions and delivery with the director and post-production. | vodja montaže oziroma obdelave zvoka |
| **dialogue editor** | Selects, organises and repairs dialogue recordings, preparing coherent material for the mix. | montažer dialoga |
| **sound-effects editor** | Selects, creates and arranges effects and backgrounds in relation to picture and the sound plan. | montažer zvočnih učinkov |
| **Foley artist** | Performs synchronised physical sounds for recording, working with the Foley recording and editorial team. | izvajalec sinhronih zvočnih učinkov |
| **re-recording mixer / dubbing mixer** | Balances and processes prepared sound elements into the final mix with creative and delivery requirements in view. | tonski mojster končne zvočne mešanice |
| **ADR** | Dialogue recorded again or additionally after filming, commonly aligned to the performance on screen. | naknadno snemanje oziroma nadomeščanje dialoga |
| **Foley** | Sound performed and recorded in relation to picture, often footsteps, movement or object handling. | naknadno izvedeni sinhroni zvočni učinki |
| **soundtrack** | The whole sound component of a film or programme; specify when referring only to a music release. | celotna zvočna podoba; kontekstualno glasbena izdaja |
| **score** | Music composed for the work, distinct from its complete soundtrack. | izvirna filmska glasba |
| **stem** | A separately supplied mix of related sound elements, such as dialogue, music or effects. | ločena skupinska zvočna mešanica |
| **music and effects / M&E** | A version or set of elements retaining music and effects for uses such as replacing dialogue in another language. | glasba in učinki brez izvirnega dialoga |
| **voice-over / VO** | Speech presented over images, commonly as narration or commentary; distinguish it from dialogue spoken off screen within the current scene. | spremljevalni govor; glasovna pripoved |
| **off-screen dialogue / O.S.** | Speech from a character in the scene's location who is outside the frame at that moment. | govor osebe v prizoru zunaj kadra |

A production sound mixer records on location; a re-recording mixer combines and finishes sound in post-production. The word **mixer** alone does not identify which stage someone means. **Dubbing mixer** is a conventional professional title and does not imply that the person works only on translation into another language.

ADR is not the same as Foley: replacing a spoken line and performing footsteps solve different problems. Expansions of *ADR* vary in professional usage, so explaining the actual process is more useful than insisting on one expansion. A Foley artist performs sound events; an effects editor may also use recordings from other sources. Both can contribute to the same finished moment.

An unseen speaker does not automatically make a line voice-over. In screenplay notation, distinguish narration or another designated V.O. use from a character speaking outside the frame within the scene. Chapter 13 explains this distinction; see also [Final Draft's guidance on V.O. and O.S.](https://www.finaldraft.com/blog/how-to-use-voice-over-in-a-screenplay-formatting-and-best-practices-explained).

Sources: ScreenSkills, [Supervising sound editor](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/post-production/supervising-sound-editor/), [Dialogue editor skills](https://www.screenskills.com/skills-checklists/unscripted-tv/post-production-department/dialogue-editor-skills/), [Sound-effects editor skills](https://www.screenskills.com/skills-checklists/unscripted-tv/post-production-department/sound-effects-editor-skills/), [Foley artist](https://www.screenskills.com/job-profiles/browse/post-production/sound-studios/foley-artist-post-production/) and [Dubbing mixer](https://www.screenskills.com/job-profiles/browse/post-production/sound-studios/dubbing-mixer-post-production/).

### Colour and visual effects

Colour and effects work require precise references to the approved version and source material. Distinguish the camera image, the viewing transform and the rendered delivery when identifying a problem.

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **colourist / colorist** | Shapes and matches the finished colour appearance with the director, DoP and finishing team. | kolorist; oblikovalec končne barvne podobe |
| **VFX supervisor** | Oversees visual-effects planning and execution, coordinating the required imagery with directing, cinematography and effects teams. | vodja vizualnih učinkov |
| **compositor** | Combines image elements into an integrated shot, matching their perspective, edges, movement and appearance. | sestavljalec slikovnih elementov; kompozitor slike |
| **colour correction** | Adjustments addressing balance or consistency; often part of the wider grading process. | barvna korekcija |
| **colour grading** | The broader shaping of colour and tonal appearance across the work. | oblikovanje končne barvne in tonske podobe |
| **look-up table / LUT** | A defined numerical mapping used to transform values; it may serve a technical or creative purpose. | preslikovalna tabela |
| **plate** | An image element recorded or prepared for use in a composite; identify which version and purpose. | slikovna podlaga za sestavljanje učinkov |
| **matte** | An image or mask defining which areas contribute to a combination or adjustment. | maska za izločanje oziroma združevanje delov slike |
| **keying** | Isolating image regions using a property such as colour or brightness. | izločanje delov slike po barvi oziroma svetlosti |
| **tracking / matchmoving** | Estimating movement so added or modified elements maintain the intended relationship to the recorded image. | sledenje gibanju; uskladitev virtualne kamere |
| **practical effects / SFX** | Effects physically produced for filming; they may be combined with later visual-effects work. | fizično izvedeni posebni učinki |

“Apply the LUT” is incomplete when several transforms exist. Name the intended input and result: a viewing conversion and a creative look need not be the same transform. A LUT also does not replace shot-by-shot judgement. **Colour correction** and **grading** overlap in workplace usage; ask what work is included instead of treating the distinction as an absolute boundary between jobs.

**VFX** and **SFX** are useful distinctions, but abbreviations need context: *SFX* can also mean *sound effects* in an audio discussion. Write the full term where confusion is possible. A tracking task might concern a two-dimensional object in an image or reconstructing camera movement; describe the required result.

Sources: ScreenSkills, [Colourist skills](https://www.screenskills.com/skills-checklists/unscripted-tv/post-production-department/colourist-skills/), [VFX supervisor](https://www.screenskills.com/job-profiles/browse/visual-effects-vfx/on-set/vfx-supervisor/) and [Compositor](https://www.screenskills.com/job-profiles/browse/visual-effects-vfx/compositing/compositor-visual-effects-vfx/); Adobe, [Compositing overview](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-composites/compositing-overview.html); ARRI, [Editorial workflow](https://www.arri.com/en/learn/camera-systems/pre-postproduction/editorial-workflow) and [Visual-effects FAQ](https://www.arri.com/en/learn-help/learn-help-camera-system/image-science/vfx-faq).

### Television studio, gallery and live production

Television work adds terminology for controlling several sources and coordinating events in real time. A **gallery** in British television usually means a production control room, not a public exhibition space. A programme can be recorded with a live production method without being transmitted live.

| English term | Meaning and professional relationship | Slovene orientation |
| --- | --- | --- |
| **studio director** | Directs the programme's audiovisual execution, coordinating cameras, switching, sound, timing and floor activity. | televizijski režiser |
| **floor manager** | Relays the director's cues and coordinates activity on the studio floor with performers and floor personnel. | vodja studia; povezava med režijo in studiem |
| **vision mixer** | Selects and combines picture sources at the switcher in response to the director's plan and cues. | operater slikovne mešalne mize |
| **gallery PA / script supervisor** | Tracks programme timing, script and cues for the gallery team; the role differs from film continuity supervision. | spremljanje scenarija in časov v televizijski režiji |
| **presenter / host** | Leads the audience through the programme, working with editorial and studio direction. | voditelj, voditeljica |
| **contributor** | A participant supplying knowledge, experience or other content; may be a guest, interviewee or participant. | sodelujoča oseba; gost; sogovornik |
| **gallery / control room** | The operational space from which a studio or outside-broadcast production is controlled. | televizijska režija |
| **rundown / running order** | The ordered list of programme items, with timing and operational information. | vrstni red in časovni potek oddaje |
| **cue** | A signal to perform a specified action at the required moment. | znak za začetek oziroma dejanje |
| **VT / package** | Recorded material inserted into a programme; *VT* persists even where no videotape is used. | vnaprej posnet prispevek |
| **autocue / teleprompter** | A display presenting text where the presenter can read it while maintaining the intended eyeline. | zaslon za branje besedila ob kameri |
| **talkback / intercom** | The communication system linking production personnel during the programme. | interna govorna komunikacija |
| **clean feed** | A feed without specified added elements; the omitted graphics or audio must be explicitly identified. | signal brez določenih dodatnih elementov |
| **tally** | An indicator showing that a source is selected or in the relevant operational state. | indikacija izbrane oziroma vključene kamere |

British **vision mixer** can name both the operator and the equipment. In some American production contexts, the operator is a **technical director**, but that title has other technical-management meanings elsewhere. A **floor manager** is not the person managing the building. A **gallery PA** may have timing and cueing responsibilities very different from a production runner's.

An instruction such as “Stand by camera two” prepares a source; the instruction that actually puts it on the programme is a separate cue under the production's calling convention. Similarly, **live**, **recorded**, and **live-to-tape** describe different relationships between performance, recording, editing and transmission. State those relationships when explaining your production method.

Sources: ScreenSkills, [Director skills](https://www.screenskills.com/skills-checklists/unscripted-tv/editorial-department/director-skills/), [Vision mixer](https://www.screenskills.com/job-profiles/browse/unscripted-tv/editorial/vision-mixer/), [Floor manager skills](https://www.screenskills.com/skills-checklists/unscripted-tv/live-studio-and-outside-broadcast-department/floor-manager-skills/), [Script supervisor skills for unscripted television](https://www.screenskills.com/skills-checklists/unscripted-tv/live-studio-and-outside-broadcast-department/script-supervisor-skills-unscripted/) and [Autocue operator](https://www.screenskills.com/job-profiles/browse/unscripted-tv/technical/autocue-operator/); Blackmagic Design, [ATEM Constellation: clean feeds and tally](https://www.blackmagicdesign.com/products/atemconstellationip/features).

### Using terminology in professional English

Terminological accuracy includes ordinary grammar and collocation. You **shoot a scene**, **record sound**, **operate a camera**, **pull focus**, **light a set**, **cut a sequence**, **mix the soundtrack**, **grade the picture**, and **deliver a master**. You can **make a film**; *do a film* gives less information about your contribution.

Support a title with concrete work: “I was the assistant editor. I synchronised the location sound, organised the rushes and prepared the sound turnover.” The second sentence demonstrates the first.

Expand an abbreviation when its meaning is not already established. **AD**, **AC**, **PA**, **TC**, **VO** and **SFX** belong to particular contexts. Check spelling against the recipient's convention: British *colour*, *programme* and *synchronise* coexist with American *color*, *program* and *synchronize*. Preserve a software control's actual spelling when referring to that control.

A useful terminology entry contains a term, a brief definition, a typical phrase and a source. Add a Slovene explanation where it resolves a distinction. Record “**picture lock — the approved picture timing used for downstream work — confirm picture lock / changes after picture lock**”, rather than only “picture lock = zaklep slike”. Understanding the responsibility and the consequence makes the term usable.

## 6. English on set and in the studio

### Make an instruction actionable

An instruction should identify the action and, when necessary, the object, location, timing or condition. Compare *Move it* with *Move the chair to the mark beside the window*. The second sentence supplies the information required to carry out the action.

In audiovisual work, an instruction often describes a relationship:

> Begin the movement after the actor looks towards the door.  
> Keep the microphone out of frame.  
> Hold the framing until the actor has left the shot.  
> Leave a short pause before the next question.

Expressions such as *before, after, until, while* and *once* establish sequence. *Towards, away from, above, below, in front of* and *behind* establish spatial relationships. If a direction could be interpreted from different viewpoints, specify the viewpoint: *camera left* or *the performer's left*.

This chapter concerns the English used to communicate an instruction. Actual equipment operation and safety procedures follow the responsible department's instructions.

Ceramella and Lee connect the language of instructions with briefing and practical production situations (2008, pp. 24–27, 44–49).

### Distinguish direction from method

A desired result and a method of achieving it are different:

> We need the face to remain visible when she turns.  
> Could you suggest a lighting adjustment that would achieve that?

The first sentence describes the result. The second asks the relevant specialist to identify a method. When you do specify a method, make its status clear:

> One option would be to change the angle.  
> I suggest testing a wider framing.  
> The brief requires the sign to remain readable.

*One option* introduces a possibility; *I suggest* makes a recommendation; *requires* states a condition imposed by the brief. Avoid presenting a personal preference as an external requirement.

### Describe a shot precisely

Identify the subject, framing, movement and relevant action. Include the purpose if you are explaining a creative choice.

> The shot begins on an empty chair. The camera tilts up as the character enters and settles on a medium shot. The movement delays our view of her face until she has noticed the letter.

The first two sentences describe the proposed image and movement. The last explains the intended effect. A technical description and an interpretation can therefore coexist without being confused.

Distinguish moving the camera through space from changing focal length. A zoom changes the framing through the lens; physically moving the camera changes its position. The resulting images can differ in spatial relationships and perspective. Chapter 5 explains the relevant terminology.

When giving a note, use only the dimensions that matter. A long list of technical details can obscure the actual decision:

> Please identify the moment when the frame begins to widen. We need to decide whether that change should follow the character's glance.

### Report a problem without inventing a cause

A useful report gives:

1. The item or version being checked.
2. The location of the issue.
3. The observable symptom.
4. What has already been checked.
5. The action or decision needed.

> In the review file named *Interview_v03*, the picture freezes briefly just after the second question. The source clip plays normally in the source viewer. Please check whether the problem is present in your copy before we create another export.

The report separates an observed freeze from the unconfirmed cause. It also identifies a useful next check.

Use *appears, seems, may* and *might* when the evidence is incomplete. Use a direct statement when the observation has been checked:

> The copied file is smaller than the file on the source drive.  
> The difference may explain why the transfer check failed.

The first sentence reports a comparison. The second proposes an explanation.

### Confirm the extent of a change

A change often has consequences beyond the immediate instruction. Describe what changes, what the change affects and which decision remains open.

> The interview will now be filmed indoors. The questions and intended duration remain the same. We need to check the new room before confirming the camera and sound arrangements.

*Remain the same* explicitly preserves part of the earlier plan. *Before confirming* prevents an unresolved arrangement from sounding final.

Use *instead of* to replace an action, *in addition to* to add one, and *rather than* to contrast two alternatives within an actual decision:

> Record the introduction in the foyer instead of the auditorium.  
> We need the room's background sound in addition to the interview.  
> The brief asks for an explanation of the process rather than a promotional slogan.

Be especially careful with *also* and *only*. *Also replace the opening title* adds a task. *Replace only the opening title* limits the scope.

### Spoken cues and their context

Production teams use established cues, but their exact wording and sequence vary. Learn the sequence used by the responsible people on the production. Recognise the purpose of a cue: asking for readiness, identifying a recording, starting an action, ending an action or moving to another task.

The terms *stand by, rolling, action, cut* and *wrap* can be important in the appropriate setting. *Stand by* asks someone to be ready. *Rolling* indicates that recording is under way in the stated department. *Action* cues the intended action when used by the person responsible. *Cut* ends the take in that context, while *cut* in an editing note may name a transition or an edit decision. *Wrap* needs a scope: a performer, a location, the day or principal photography.

A student should be able to explain the function of a cue and recognise its context. Memorising an isolated word does not establish when you are authorised to use it.

In a television gallery, *cue* can be a noun or a verb: *wait for the cue* and *cue the presenter*. A *running order* establishes the planned sequence of items. *Live* and *recorded* describe different transmission or production circumstances; they do not by themselves explain the entire workflow. See Ceramella and Lee (2008, pp. 18–24, 42–43) for related broadcast language.

### Give a concise handover

A handover enables the next person to continue accurately. Identify the version, completed work, outstanding issues and next action.

> This is version 4 of the sequence. The replacement interview shot is included, and the title spelling has been corrected. The final music choice is still pending. Please review the transition into the closing scene; I have placed a marker at the point that needs a decision.

Useful expressions include *has been completed, remains provisional, is awaiting approval, still needs checking, is ready for review*. These describe different states. *Ready for review* should not be rewritten as *approved*.

End with a specific request when a decision is needed:

> Please confirm which of the two endings you want developed further.  
> Could you identify the preferred take before I revise the sequence?  
> I need the correct spelling of the contributor's name before updating the title.

## 7. Working in English

### Communication begins with a purpose

Professional English enables another person to understand something and act on it. Before speaking or writing, identify your purpose. Are you reporting an observation, asking for a decision, explaining a procedure, recommending a change or confirming an agreement? These purposes require different language.

Consider three sentences about the same shot:

> The camera moves towards the window.  
> The camera movement draws attention to the window.  
> Could we begin the camera movement after she turns?

The first describes something observable. The second interprets its effect. The third proposes an action. A useful explanation makes the relationship between observation, interpretation and proposed action clear. This distinction matters in technical notes, creative feedback and assessments of a film.

Precision includes knowing how much you know. If you have observed a problem but have not established its cause, say so:

> The dialogue drops out between 00:01:12 and 00:01:14 in the review file. I have not checked the source recording yet.

This gives the recipient a location, a symptom and the limit of the investigation. The sentence does not prematurely identify a recording fault.

Ceramella and Lee introduce clarification, definitions and problem descriptions through professional situations (2008, pp. 64–69). These functions recur throughout this course.

### Describe your role through actions

A job title gives a broad indication of responsibility. An explanation of what you actually do makes that title meaningful. Use verbs that identify the work: *plan, direct, light, frame, record, select, assemble, synchronise, revise, coordinate, monitor, deliver*.

> I study cinematography. On this project, I am responsible for the visual approach and the camera work. I am testing how changes in lighting affect the faces in the interview scenes.

> I am editing the documentary. I organise the material, compare alternative sequences and discuss the structure with the director. The current version concentrates on the protagonist's working day.

> I am directing a short film. I am developing the performances and the visual treatment with the other departments. At present, I need to clarify how the final scene changes the audience's understanding of the opening.

Notice the distinction between a regular role and current work. *I edit documentaries* describes a general activity; *I am editing a documentary* describes a current project. *I have edited the interview* reports a completed action with a present consequence.

Be accurate about authorship and responsibility. *I worked on the sound* may cover many tasks. *I recorded the location dialogue* and *I edited the dialogue tracks* identify different contributions.

### Explain a term at the right level

A useful definition identifies a category and a distinguishing function:

> A call sheet is a production document that gives the people involved the information they need for a particular shooting day.

An example can then make the definition concrete:

> It may tell an actor when and where to report, identify the scenes scheduled for the day and provide the relevant contact information.

For a specialist audience, a familiar term can stand alone. For a non-specialist listener, define it briefly on first use:

> We created lower-resolution editing copies, or proxies, so that the editor could work smoothly with the footage.

Avoid using a near-synonym that changes the concept. A *take* is not simply another word for a *scene*. A *producer* and a *director* do not name the same role. Chapter 5 develops these distinctions by profession.

Slovene equivalents in this material are orientation aids. Credit conventions and the division of work vary between countries and productions. When a title has no exact equivalent, explain its responsibilities before choosing a translation.

### Register: language appropriate to the situation

Register concerns the language appropriate to a purpose, audience and relationship. It includes vocabulary, sentence structure, directness and the amount of explanation.

| Situation | Appropriate example | What the wording does |
| --- | --- | --- |
| Immediate technical clarification | “Which channel are you monitoring?” | Asks a narrow question quickly. |
| Request to a colleague | “Could you send the revised shot list before the location visit?” | Identifies the item and the relevant deadline. |
| First contact with an external collaborator | “I am contacting you about the sound post-production for our short film.” | Establishes the reason for writing. |
| Creative suggestion | “Holding this shot longer may make her hesitation easier to read.” | Connects a proposed change to an intended effect. |
| Unconfirmed explanation | “The discrepancy may come from different export settings.” | Marks a possibility rather than a finding. |
| Confirmed agreement | “We agreed to review version 3 on Thursday.” | Records a decision already made. |

Politeness does not require lengthy, vague sentences. *Could you possibly perhaps try to send it whenever you have a moment?* hides the practical need. A clear request with a reasonable explanation is easier to answer.

Directness should also fit the setting. A short instruction can be appropriate during a time-sensitive operation; an explanation of a disputed creative decision usually needs more context. Avoid assuming that a colleague's accent, brevity or unfamiliar phrasing reveals their attitude.

### Clarification is a professional skill

If an instruction is ambiguous, locate the ambiguity. *I do not understand* is a useful beginning, but a focused question moves the work forward.

| Need | Useful language |
| --- | --- |
| Identify a referent | “When you say ‘the first version’, do you mean the file sent on Monday?” |
| Check a term | “Are you using ‘master’ to mean the final approved export?” |
| Check a quantity | “Is that fifteen frames or fifteen seconds?” |
| Check a relationship | “Should the sound change begin before the cut or at the cut?” |
| Check a requirement | “Is this a requirement for delivery or a suggestion for the review copy?” |
| Confirm an action | “So I will revise the opening and leave the ending unchanged.” |
| Admit a limit | “I have not checked that yet. I can confirm it after reviewing the source file.” |

Do not repeat a whole message when only one part is unclear. Quote or paraphrase the relevant part and ask the question that will resolve it.

### A complete professional response

An effective response usually contains four elements: what you understand, what you can do, what remains uncertain and what happens next.

> I understand that you need a shorter version for the presentation. I can reduce the introduction and retain the complete interview answer. Please confirm whether the title sequence counts towards the requested duration. Once that is clear, I can give you a reliable delivery time.

This is more useful than a promise made before the requirements are understood. It also distinguishes a commitment from an estimate. *I will send it by noon* commits to a deadline; *I expect to send it by noon* communicates an expectation; *I can send it by noon if the revised titles arrive this morning* states a condition.

In every chapter, pay attention to these small differences. They determine whether the recipient understands a sentence as an observation, a possibility, a request or a promise.

## 8. Reading, listening and checking sources

### Identify the kind of text

A technical manual, a film review, an interview and a production brief can discuss the same subject while doing different things. A manual explains operation; a review evaluates; an interview presents a person's account; a brief specifies the work to be done. Your reading strategy should follow the document's purpose.

Start with four questions: who produced the text, for whom, for what purpose and in what context? Then identify what you need from it. You may need an instruction, an argument, a definition, a deadline or a statement you can check against another source.

Ceramella and Lee use professional texts to connect vocabulary with practical reading: production documents in the television unit, screenplays and query letters in the film unit, and reviews that require interpretation as well as comprehension (2008, pp. 42–62).

### Read for structure before detail

First establish the overall task or argument. Then look for information that changes an action or interpretation. In a brief, these are often the deliverable, audience, duration, responsibilities, dates and constraints. In a review, they include the main judgement, the evidence offered for it and any qualification.

Consider this original production brief:

> The archive needs a three-minute English introduction to its collection for visitors who have no specialist knowledge of film preservation. The film should explain what the collection contains and show one example of how an item is identified. Interview material may be used, provided that the explanation remains accessible. The first version is for internal review. A public release will be considered after the archive checks the factual information.

The **purpose** is to introduce a collection. The **audience** consists of non-specialists. The **content requirements** are the collection's scope and an identification example. The word *may* makes interview material optional. *Provided that* introduces a condition. The first version is a review version, and public release is a later decision.

A summary that says “Make a public promotional film with interviews” would misrepresent several parts of this brief. Accurate reading preserves the difference between a requirement, an option and a condition.

### Separate evidence from evaluation

Read the following original review passage:

> The film keeps returning to the empty ticket window. These repetitions slow the narrative, but they also give the building a presence that the dialogue rarely acknowledges. In the final scene, the window is shown from the street for the first time. That change in viewpoint makes the departure feel more decisive than the character's closing speech.

“The film keeps returning to the empty ticket window” is an observation that can be checked. “Slow the narrative” is an interpretation of rhythm. “Give the building a presence” is a more abstract interpretation. The final sentence compares the effects of image and speech.

A useful response identifies the evidence and explains why it supports, or fails to support, the judgement. *The review says the film is good* discards the argument. *The reviewer argues that the change in viewpoint carries the emotional conclusion more effectively than the dialogue* preserves it.

Use attribution when reporting an interpretation:

> The reviewer argues that …  
> The director describes the scene as …  
> The interview suggests that …  
> According to the production notes, …

Attribution does not automatically establish that the statement is correct. It tells the reader whose claim is being reported.

### Read specifications literally

Small grammatical choices can determine whether a file satisfies a brief. Compare:

| Wording | Meaning |
| --- | --- |
| “The review file must include subtitles.” | Subtitles are required. |
| “The review file may include subtitles.” | Subtitles are permitted. |
| “The review file should include subtitles.” | Subtitles are recommended; check whether the brief uses *should* as a requirement. |
| “Subtitles must be supplied separately.” | The subtitle deliverable must be separate; this does not by itself settle whether a viewing copy also needs visible subtitles. |
| “Do not include the temporary music.” | The temporary music must be excluded. |
| “The duration must not exceed three minutes.” | Three minutes is an upper limit. |

Write down uncertainties before beginning work. Do not treat a missing specification as permission to choose any value. Ask a focused question about what matters to the recipient.

### Listening for decisions

When listening to a technical explanation or a project presentation, record decisions and their reasons. A useful note contains an action, its owner, its timing and any condition. A complete transcript is rarely necessary for this purpose.

Suppose the lecturer reads:

> The opening remains as it is. Please replace the temporary title with the approved title. The producer has not confirmed the end credits yet, so keep the current credit sequence in the review copy and mark it as provisional.

Useful notes would distinguish the confirmed title change from the unresolved credits. Writing “Replace titles and credits” would erase that distinction.

Listen for contrast and qualification: *however, although, unless, only if, for the moment, subject to confirmation*. These expressions often contain the information that prevents a misunderstanding. Ceramella and Lee's work on briefing, instructions and debriefing provides related practice (2008, pp. 24–29).

When listening to an interview, distinguish what the speaker says they intended from what the finished work actually does. An account of an intention is evidence about that intention; the effect on an audience still requires interpretation.

### Check terminology in a relevant source

Begin with the term, the department and the context. A general dictionary can establish ordinary meanings, but a professional manual or role profile can establish a specialised use.

For example, *grade* can refer to an assessment mark or to colour work; *strike* can refer to industrial action or, in a production context, taking something down; *wrap* concerns the completion of a defined period or part of production. Do not select the first dictionary meaning without checking the surrounding sentence.

A small terminology record is useful:

| Field | What to record |
| --- | --- |
| Term | The expression exactly as used. |
| Field and context | Camera, editing, production, sound, or another relevant area. |
| Meaning | A concise definition in English. |
| Example | An original sentence showing the intended use. |
| Source | Author or organisation, page or URL, and version/date when relevant. |
| Slovene orientation | A suitable equivalent or a description of the function. |

Professional roles can vary with region, budget and production type. Distinguish the role's function from the particular credit used on one project. Chapter 5 identifies several cases where this matters.

### Evaluate an online explanation

Check whether an explanation is a manufacturer instruction, a professional association's description, a personal account, an advertisement or an anonymous summary. Each may be useful for a different question.

For a technical instruction, verify the product and version. For a festival requirement, verify the edition and submission category. For a subtitle specification, verify the provider, language and type of subtitles. A rule for one deliverable should not silently become a general rule for all audiovisual work.

An older textbook remains useful for many communicative functions and terms. Its references to particular recording media, delivery systems or services need their historical context. When current operation matters, consult the relevant current documentation.

### Check a machine translation or AI revision

Compare the revised sentence with the original intention. Check the nouns and verbs that carry the professional meaning, all numbers and negations, and words that indicate obligation or uncertainty.

Original intention:

> The director has not approved the revised ending. We can prepare a review copy, but we cannot describe it as the final version.

Faulty revision:

> The director has approved the revised ending, and we can prepare the final version.

The revision is fluent and reverses the meaning. A subtler error would preserve the first sentence but replace *review copy* with *master*. Check the function of the deliverable as well as the grammar.

For any suggested source, open the source and check that it exists and supports the claim. For a suggested term, inspect examples from the relevant professional field. Treat the result of the check as the basis of your decision.

## 9. Production documents and technical information

### Documents organise different decisions

A production brief explains the intended work and its constraints. A schedule allocates time and resources. A call sheet supplies information for a particular shooting day. A shot list describes planned shots. A camera report or footage log records information about material that has been captured. An editing memo gives decisions or instructions concerning an edit.

The same production may use different templates. Read the fields and their purpose before assuming that a familiar heading has a universal meaning. Ceramella and Lee treat schedules, location arrangements and written editing instructions in the television unit (2008, pp. 44–51).

### A brief should answer practical questions

A clear brief identifies the purpose, intended audience, deliverable, required content, constraints, review process and responsibility for decisions. It may also identify material already available and dependencies that affect completion.

**Original model brief: an archive introduction**

| Field | Information |
| --- | --- |
| Purpose | Introduce a small film archive to first-time visitors. |
| Audience | Visitors who do not have specialist knowledge of film preservation. |
| Deliverable | An English viewing copy for internal review, approximately three minutes long. |
| Required content | The collection's scope; one example of identifying an item; a clear closing invitation to learn more. |
| Available material | Approved photographs of the storage area and an interview with an archivist. |
| Editorial approach | Explain specialised terms on first use. Retain qualifications concerning uncertain dates and attributions. |
| Review | The archivist checks factual information; the project lead confirms the final sequence. |
| Outstanding decision | Whether an additional demonstration can be recorded. |

The last field matters. A pending decision should not disappear when the brief is summarised. Similarly, *approximately three minutes* allows a degree of flexibility that *no longer than three minutes* does not.

### Read a schedule as a set of dependencies

A schedule is more than a list of times. It connects activities with people, places, resources and prior decisions. Distinguish the time when someone must arrive from the time when recording begins.

**Fictional schedule excerpt**

| Time | Activity | Dependency or note |
| --- | --- | --- |
| 08:30 | Crew arrival and access check | Location representative opens the building. |
| 09:00 | Prepare the interview area | Subject arrives at 09:30. |
| 09:45 | Record the interview | Proceed after the subject and technical departments are ready. |
| 11:00 | Record collection details | The archivist identifies the permitted items. |
| 12:00 | Review remaining requirements | Check that the planned material has been obtained. |

A sentence such as “The archivist arrives at nine” would be unsupported by this excerpt. The table gives the subject's arrival and an archivist's role, but it does not establish that these are the same person.

Read labels carefully: *arrival, call time, preparation, rehearsal, recording, review* and *departure* name different events. Report a conflict by referring to the affected activity:

> The interview is scheduled to begin at 09:45, but the subject is now available only from 10:15. We need to revise the activities that depend on the interview.

### Write a useful shot list

A planned shot list can identify the scene, shot, subject/action, framing or movement, and a relevant sound or continuity requirement. Choose the detail that the intended readers need.

**Fictional planned shots**

| Shot | Image and action | Relevant note |
| --- | --- | --- |
| 1 | Wide view of the entrance before visitors arrive. | Establish the location. |
| 2 | Close view of a labelled film can as the archivist places it on the table. | The label must be readable in the proposed framing. |
| 3 | Medium interview framing of the archivist. | Include enough context to identify the setting. |
| 4 | Detail of the catalogue entry being checked. | Use the example approved for the explanation. |

A later footage log would record what was actually captured, with the identifiers used by the production. Keep the planned shot number distinct from a take number and from the media filename. One planned shot may have several takes; a recorded take may contain material useful in more than one part of an edit.

### Describe deliverables without ambiguity

Terms such as *high quality, normal format, small file* and *the usual settings* need context. When a specification is important, name the required property and its value.

Common fields include container, video codec, frame size, frame rate, scan type, audio arrangement, subtitle arrangement, duration, filename and purpose. A container and a codec identify different aspects of a file; an extension alone does not establish every stream's encoding or properties.

**Fictional review-copy requirements for a classroom task**

| Property | Requirement in this example |
| --- | --- |
| Purpose | Internal review of picture, dialogue and title wording. |
| Container | MP4. |
| Video codec | H.264. |
| Frame size | 1920 × 1080 pixels. |
| Frame rate | 25 frames per second, progressive. |
| Audio | A stereo review mix. |
| Visible text | English subtitles visible in the picture for this review. |
| Filename | Project title, version number and the word “review”. |
| Approval status | Unapproved review copy. |

These are the invented requirements of this example. They are not a general festival, broadcaster or archive delivery standard. An actual delivery brief may request different values and additional properties.

If a brief specifies something you cannot establish, ask:

> Do you need a stereo review mix or separate audio components?  
> Should the subtitles be visible in the picture or supplied as a separate file?  
> Which delivery specification should we follow for the final approved version?

Do not infer a final delivery requirement from a temporary review arrangement.

### Read time references correctly

Time references can use elapsed time, frame-based timecode or a subtitle format. Identify the notation before interpreting it.

In a **25 fps, non-drop-frame** sequence starting at *00:00:00:00*, the timecode *00:00:12:10* identifies 12 seconds and 10 frames after the start, or 12.4 seconds. The last field is a frame count. In an SRT subtitle timestamp, *00:00:12,400* means 12 seconds and 400 milliseconds. With both references starting at zero, the examples identify the same elapsed point, but their notation is different.

Frame rate and timecode conventions become essential when moving between systems. For this course, label the convention used in a task and avoid converting a frame field as though it were a decimal fraction.

When writing an editing note, identify the version and whether the reference is to the source clip or the sequence:

> In sequence version 5, at 00:00:12:10 on the 25 fps sequence timecode, the title appears before the archivist finishes naming the collection.

A time reference without the version or time base can send the recipient to the wrong place.

For the structure of SubRip timestamps and cues, see the Library of Congress's description of the [SubRip subtitle format](https://www.loc.gov/preservation/digital/formats/fdd/fdd000569.shtml).

### Version names should reveal the state of the work

A useful filename identifies the project, type of deliverable and version:

> ArchiveIntro_edit_v03_review.mp4  
> ArchiveIntro_subtitles_v03_en.srt  
> ArchiveIntro_notes_v03.docx

Agree a consistent naming pattern and use it. A label such as *final_final_reallyfinal* does not reliably identify approval. Version numbering and approval status are related but different: version 5 can still be provisional.

In a message, describe the change:

> Version 3 includes the corrected name title and the shorter introduction. The interview content is unchanged.

This allows the reviewer to focus on the relevant decisions. Preserve an earlier version when it is needed to understand or restore a decision.

### Write an editing or delivery memo

A useful memo separates confirmed actions, unresolved questions and observations.

**Original model memo**

> **Subject: Archive introduction — review of version 3**
>
> **Confirmed changes:** Replace the opening title with “Inside the Film Archive”. Correct the contributor's surname in the lower-third title.
>
> **Question for the project lead:** The current opening explains the building before introducing the collection. Should we test an alternative that begins with the film can?
>
> **Technical observation:** The word “collection” is difficult to hear in the second interview answer. Please compare the source audio with the review mix before deciding whether a different take is needed.
>
> **Next version:** Prepare a review copy after the title corrections. Keep the alternative opening as a separate option until it has been reviewed.

The memo identifies different kinds of information. A question remains a question; an observation does not become a confirmed diagnosis; an optional opening does not silently replace the approved structure.

## 10. Emails and international collaboration

### Make the purpose visible

A professional email should enable its reader to identify the subject, understand the situation and act. State the purpose early. Include background only to the extent that it explains the request or decision.

A useful sequence is **purpose, essential context, requested action, timing**. The order can change when the relationship or circumstances require it, but none of the essential information should be hidden.

Ceramella and Lee compare professional email registers and the information required in a brief (2008, pp. 35–38). Their query-letter work also illustrates the importance of identifying the project and the action requested from the recipient (pp. 55–56).

### Subject lines and openings

The subject line should name the project and purpose:

> Archive introduction — title corrections for version 3  
> Location visit — confirmation needed for 12 May  
> Short film — question about the subtitle deliverable

Avoid a subject line that is so broad that the message cannot be distinguished from the rest of the correspondence. If a continuing thread has moved to a substantially different topic, update the subject or begin a clearly identified message.

Use a greeting appropriate to the relationship. *Dear Ms Novak* is a formal opening when the name and title are known. *Dear Alex* or *Hello Alex* may be appropriate in established professional contact. Address a person in the way they have indicated, and avoid inventing a title.

An opening can establish purpose directly:

> I am writing to confirm the arrangements for the interview.  
> Thank you for the revised brief. I have one question about the delivery format.  
> I am contacting you about the possibility of recording an interview for our student film.

### Request information precisely

**Original model email**

> **Subject: Archive introduction — confirmation of review requirements**
>
> Dear Alex,
>
> Thank you for sending the brief. We are preparing the first review copy and would like to confirm two details.
>
> Should the three-minute duration include the opening title and end credits? Also, would you prefer the English subtitles to be visible in the review picture or supplied as a separate file?
>
> We can complete the review copy once these points are clear. Could you send your preference by Wednesday at 12:00, Ljubljana time?
>
> Best regards,  
> Nika

The questions concern two specific ambiguities. The message gives a reason for asking and a clear time reference. It does not imply that a final delivery specification has already been agreed.

Use *could you confirm whether …* or *could you let me know which …* for indirect questions. The word order inside the indirect question is that of a statement:

> Could you confirm **when the interview begins**?  
> Could you explain **which version you reviewed**?

### Confirm an agreement

An agreement confirmation should state what was decided, who will act and what remains unresolved.

> Thank you for confirming the arrangements. We will meet at the main entrance at 09:00 on 12 May. You will identify the collection items before recording begins. We will send the factual review copy after the interview has been edited. The public-release date remains to be agreed.

Writing *everything is confirmed* would conceal the unresolved release date. Use phrases such as *as agreed, to confirm our conversation* and *the following remains open* only when they accurately describe the state of the agreement.

Spell out potentially ambiguous dates. *12 May 2027* is easier to interpret internationally than *12/05/27*. When an exact time matters across countries, state a location or time zone. Take seasonal clock changes into account when arranging an actual appointment.

### Explain a problem and propose the next step

**Original model email**

> **Subject: Interview review copy — revised delivery estimate**
>
> Hello Alex,
>
> We have completed the picture changes, but the approved name titles arrived later than expected. I still need to insert them and check their spelling against your list.
>
> I can send a review copy with provisional titles this afternoon, or a fully checked version tomorrow morning. Please let me know which would be more useful for your review.
>
> I am sorry for the change to the original timing. I will confirm the delivery time as soon as I receive your preference.
>
> Best regards,  
> Nika

The message identifies what is finished, explains the remaining dependency and offers two feasible next steps. It uses a concise apology without allowing the apology to replace practical information.

Do not give an exact promise simply to make a message sound reassuring. State a realistic commitment or an estimate with its condition.

### Disagree clearly and professionally

A useful disagreement identifies the issue and gives a reason:

> I understand the need to shorten the sequence. Removing the second answer, however, would leave the speaker's conclusion without its explanation. Could we first reduce the introduction and review the duration again?

The response acknowledges the aim, identifies the consequence of one proposal and offers an alternative. *That will not work* gives less information. *I completely agree, but …* may misrepresent your position.

Different situations require different degrees of firmness:

| Purpose | Example |
| --- | --- |
| Offer an alternative | “Another option would be to shorten the opening.” |
| Express a reservation | “I am not yet convinced that this version makes the sequence clearer.” |
| Explain a practical limit | “We cannot complete that revision before receiving the approved text.” |
| Correct a misunderstanding | “The file sent on Monday was a review copy. It was not identified as approved for release.” |
| Decline a request | “I am unable to take on the additional edit within the proposed period.” |

Avoid unnecessary intensifiers such as *obviously* and *clearly* when they imply that a reasonable question should not have been asked. Describe the evidence or requirement.

### Follow up without changing the agreement

A follow-up names the earlier request and explains why a response is now needed:

> I am following up on the subtitle question below. We need the decision before preparing the review copy. Could you confirm your preference by tomorrow at 10:00?

If the deadline is new, identify it as a request. Do not write *as agreed* for a deadline that was never agreed.

When forwarding information, say why it is relevant:

> I am forwarding the revised location note. Please check the access information before the visit.

When attaching a document, name it and explain its state:

> Attached is the revised brief, version 2. The new section identifies the two decisions that still need confirmation.

### Check the email before sending

Read the message once for meaning and once for practical details. Check the recipient, subject, attachment or link, version, names, dates and requested action. Confirm that the wording preserves any uncertainty or condition.

Then ask whether the recipient can answer the request without guessing what *it, that, the file* or *the last version* refers to. Replace an ambiguous reference with a short, exact description.

## 11. Describing stories and presenting projects

### Different texts serve different purposes

A project description, logline, synopsis, treatment, statement and pitch overlap in content but serve different purposes. Learn what the reader needs from each.

| Term | Main function |
| --- | --- |
| Logline | Condenses a story's central situation, protagonist and conflict into a very short description. |
| Tagline | A short promotional phrase intended to attract interest; it may reveal little of the actual plot. |
| Synopsis | Summarises the story or proposed work in a form and length suited to its purpose. |
| Treatment | Develops the proposed work in greater detail, often describing its progression and approach before a complete screenplay. |
| Director's statement | Explains the director's relationship to the material and the intended creative approach. |
| Pitch | Presents a project to a particular audience and gives them a reason to take the next step. |
| Query letter or email | Introduces a project briefly and requests a specific response, such as permission to send further material. |
| Press kit | A collection of information prepared to support coverage of a project or release. |

The exact requirements of a funding scheme, festival, producer or publication govern what is needed in a particular case. A synopsis for internal development may reveal the ending, while a short promotional synopsis may deliberately leave the outcome open.

Ceramella and Lee develop screenplay, query-letter and pitching tasks in the film unit (2008, pp. 53–58). Their answer key also distinguishes a logline from a tagline (p. 106). Publicity material is addressed in pp. 87–90.

### Build a logline around a clear situation

A logline helps a reader understand who is involved, what they want and what makes that aim difficult. A list of themes alone does not establish a story.

**Original fictional example**

> On the final evening of a neighbourhood cinema, an usher discovers a film addressed to her estranged mother and has one screening left in which to decide whether to show it.

The sentence identifies a protagonist, a setting with a time limit, a discovery and a consequential decision. It leaves space for development without withholding every meaningful detail.

A possible tagline for the same invented project would be:

> Some stories wait for the last screening.

The tagline suggests a tone. It does not replace the logline's explanation of the situation.

For a documentary or instructional project, forcing a fictional protagonist-conflict formula may be inappropriate. Explain the subject, question and approach:

> A short documentary follows the staff of a small film archive as they identify an unlabelled reel, showing how uncertainty is recorded rather than hidden.

### Write a synopsis that preserves cause and consequence

Use a clear sequence and identify changes in the central situation. In a conventional film synopsis, the present tense commonly describes the story: *she finds, he refuses, they return*. Use past forms when the synopsis needs to distinguish an earlier event from the story's present.

**Original short synopsis**

> On the final evening of the Aurora cinema, usher Eva is clearing a cupboard when she finds a film can addressed to her mother. Her mother stopped visiting the cinema years earlier and has never explained why. The cinema's projectionist recognises the handwriting but initially refuses to discuss it.
>
> As the final audience begins to arrive, Eva learns that the film records a performance her mother believed had been lost. Showing it could restore part of her mother's history, but it would also make a private memory public. Eva calls her mother and asks her to come. The last screening becomes a meeting between two people who have avoided the same story for years.

This model is a development synopsis. It explains the discovery, the new information and the resulting decision. Its function differs from promotional copy designed chiefly to attract an audience.

Be careful with unclear pronouns. If two characters could be the referent of *she* or *her*, repeat the name or role. Avoid introducing more names than the short text can support.

### Explain creative decisions through their intended effects

A statement should connect a decision to a purpose:

> I want the foyer to feel like a place that has been used for years. The framing will retain ordinary details around the characters, while the sound will allow activity outside the frame to remain audible.

The statement identifies an aim and the image/sound choices intended to support it. It is more informative than *The cinematography will be beautiful and atmospheric*.

Use a careful relationship between intention and effect:

> We intend the repeated framing to suggest …  
> The contrast is designed to draw attention to …  
> This approach may encourage the viewer to notice …  
> In the current version, the transition appears to …

An intention is not proof of a successful effect. In a presentation, be ready to identify the evidence in the material you show.

### Organise an individual presentation

A clear project presentation can answer six questions:

1. What is the project?
2. Who is it for?
3. What is the central story, question or practical need?
4. What approach are you taking?
5. What is your contribution?
6. What decision or response do you need from the listener?

State the main idea early. A long account of how you first thought of the project can delay the information the listener needs to understand the rest.

Use signposting where it helps:

> First, I will explain the project and its intended audience.  
> This example shows the problem the edit needs to solve.  
> The main difference between the two versions is …  
> I will finish by explaining the decision that remains open.

Slides or images should support your explanation. Select material you can identify and discuss precisely. If you show an image or play a clip, tell the listener what to attend to and explain its relevance afterwards.

### Answer the question asked

An answer should begin with the point that resolves the question. Add evidence or qualification afterwards.

Question:

> Why did you keep the sound from the earlier shot across the cut?

Answer:

> I wanted the change of location to feel connected rather than abrupt. The continuing sound provides that connection, while the image introduces the new space. I would still like to test whether the overlap is too long.

The answer explains the choice and acknowledges an unresolved issue. It does not evade the question by retelling the entire project.

If the question is ambiguous, clarify it:

> Are you asking about the intended effect or about how the transition was made?

If you do not know, identify the limit:

> I have not tested that version yet. My current explanation is based on the shorter transition.

### Prepare a short professional biography

A biography should identify the relevant person, role and work without unsupported claims. Use concrete information appropriate to the context.

> Eva Novak is a student of film editing in Ljubljana. Her current work explores the relationship between interviews and observational footage. She is editing a short documentary about a local film archive.

This is an invented model. In your own biography, use accurate information and a length suited to the requested format. Avoid describing yourself as *award-winning* or *internationally recognised* unless the claim is relevant and can be substantiated.

### Read publicity critically

A festival entry can show how a synopsis, credits, biography and press material perform different functions. For an authentic example, examine the [official Cannes entry for *La Chimera*](https://www.festival-cannes.com/en/f/la-chimera/). Identify which information describes the work, which identifies its contributors and which invites further attention.

When writing your own publicity text, distinguish a factual description from an evaluation. *A short documentary about a film archive* is descriptive. *An unforgettable documentary* is an evaluative claim. Select wording that suits the purpose and the evidence.

## 12. Giving feedback and discussing post-production

### Make a judgement useful

A creative judgement becomes useful when another person can understand what it concerns, what supports it and what change is being proposed. “It does not work” gives little direction. “The second explanation repeats information already clear from the image” identifies a relationship that can be examined.

Separate four elements: the location of the issue, the observation, the interpretation and the proposed action. These elements do not require four separate sentences, but they should be recoverable from the note.

> In the exchange beside the ticket window, the cut to Ivo occurs before Maja finishes her question. We therefore see his reaction while she is still speaking. This makes the exchange feel impatient to me. I would test a later cut before changing the dialogue.

The observation concerns the relationship between image and speech. The interpretation concerns impatience. The action is a test. The writer does not present a personal reading as an established fact about every viewer.

Ceramella and Lee connect feedback with follow-up action in their radio unit and develop reasoned critical judgement in the film-review section (2008, pp. 27–29, 61–62).

### Distinguish a symptom, a cause and a preference

Different kinds of note require different responses.

| Type of note | Example | What still needs to be established |
| --- | --- | --- |
| Observable discrepancy | “The name in the opening title differs from the approved credit list.” | Which document supplies the approved spelling. |
| Technical symptom | “The review file has no audible dialogue in this section.” | Whether the issue is in the file, playback, routing or source material. |
| Interpretation | “The empty room seems to represent her absence.” | Whether the film supports that reading and whether it serves the intended effect. |
| Preference | “I prefer the quieter ending.” | The reason for the preference and its relevance to the project. |
| Proposed experiment | “Try ending before the final line.” | What the alternative reveals when compared with the current version. |

Do not turn a symptom into a cause without checking it. “The microphone failed” makes a specific claim about recording. “I cannot hear the dialogue in the review file” reports what the reviewer knows. The second wording helps the relevant person investigate without committing the production to an unsupported diagnosis.

A preference can be well argued. Explain what it achieves: “I prefer the quieter ending because it leaves the character's decision unresolved.” That is more informative than implying that all quiet endings are better.

### Locate the note precisely

A useful post-production note identifies the version and location. Time references must refer to the file or sequence being reviewed. A screenshot can clarify a visual issue, but it still needs a file or version reference.

> **Review version:** last_showing_review_v03.mp4  
> **Location:** 00:02:18, as displayed in the review player  
> **Observation:** The title disappears before the speaker finishes naming the archive.  
> **Proposal:** Test a longer title duration while keeping the interview timing unchanged.

The note specifies that the time comes from the review player. It does not claim to be a frame-accurate source timecode. When precise frame identification matters, report the timecode convention and frame rate supplied by the workflow.

Avoid descriptions such as “the bit near the start” when several people are discussing different versions. Also avoid adding unsupported precision. If a location is approximate, label it as approximate.

### Compare alternatives without overclaiming

Comparisons help explain editing, framing and sound choices:

> The revised opening is shorter, but the order of information is unchanged.  
> The wider framing makes the doorway more visible.  
> The longer pause gives the reaction more emphasis.  
> The second version seems less conclusive because the answer remains unfinished.

Distinguish a measured change from an interpretation. Duration can be measured; emphasis and conclusiveness require an account of how the material creates the effect. Use *seems, suggests, may* or *in this context* when qualification is appropriate. Excessive qualification can also obscure a clear finding: if a title is misspelled against an approved list, state the discrepancy directly.

Comparative wording should identify what is being compared. “The sound is better” leaves both the criterion and the reference unclear. “The dialogue is easier to understand in version 3 because the ventilation noise is less prominent” identifies them.

### Discuss image and sound together

A shot can change meaning when its sound changes. Likewise, the effect of a sound depends partly on the image and its timing. Describe these relationships explicitly.

> We hear the projector before we see the projection room. This introduces the space through sound and prepares the visual transition.

> The outgoing scene's room tone continues briefly over the new image. The overlap connects the spaces, although the image shows that the location has changed.

> The music stops before the character answers. The resulting pause makes the answer more exposed.

The terminology in Chapter 5 helps distinguish sound overlap, dialogue editing, ambience, score and final mixing. A request to alter a sound's timing differs from a request to alter its level. “Bring it in earlier” concerns timing; “make it quieter” concerns level; “reduce its prominence” describes a perceptual aim that may require clarification.

### Explain what has changed

A revision note should connect the request to the action taken and identify anything still unresolved.

> I shortened the opening by removing the repeated view of the ticket window. The first interview answer now begins twelve seconds earlier. I retained the complete answer because its final sentence explains why the archive matters to the speaker. The spelling of one contributor's name still needs confirmation.

This account makes the revision reviewable. It identifies a structural change, a measurable consequence, a reason for retaining material and an outstanding question.

When several changes interact, identify their dependency:

> Moving this scene will change the duration before the closing sequence. If we approve the new order, the subtitle timings and the sound handover will need checking against the revised picture.

Keep a distinction between a suggestion, a tested alternative and an approved change. “We discussed removing the shot” does not mean “The shot has been removed.” “Version 4 contains the alternative opening” does not establish that it has been approved for delivery.

### Write a short critical paragraph

A critical paragraph can move from a claim to evidence, interpretation and qualification. The following is an original model:

> The final sequence gives the cinema a presence beyond its function as a setting. Earlier scenes show the foyer through the characters' movements, whereas the ending holds on the space after they leave. The continuing projector sound connects the empty image to the activity we have already seen. This combination suggests that the building retains traces of its former use. The effect depends on the length of the final hold: a much shorter shot might function mainly as a transition, while a longer one could shift attention towards the space itself.

The paragraph identifies concrete formal choices and explains a possible effect. It avoids a catalogue of disconnected adjectives. The same method supports an individual oral explanation: make the claim, identify the evidence and explain the connection.

## 13. Dialogue, scripts and subtitles

### Read a screenplay as a working text

A screenplay communicates action, setting and speech to the people developing and making a film. Its language must help the reader distinguish what happens, where it happens and who speaks. Ceramella and Lee introduce scene headings, action and dialogue, including the use of present tense, in their film unit (2008, pp. 53–55).

The following original example illustrates these distinctions. It is a readable teaching layout; submission formats and production templates may impose more detailed conventions.

```text
INT. CINEMA FOYER - EVENING

An unlit ticket window separates MAJA from IVO.
She places a dented film can on the counter.

MAJA
This was behind the screen.

Ivo turns the can so that its label faces away from her.

IVO
Then put it back.

MAJA
Without opening it?

The projector starts in the room above them.
Ivo looks towards the ceiling.
```

The heading identifies an interior, a location and a broad time. The action uses present-tense verbs: *places, turns, starts, looks*. The dialogue reveals different intentions without an explanatory paragraph about each character's feelings.

An action line such as “Ivo regrets everything” names an internal state. The example instead supplies an observable action that may support an interpretation. A screenplay can include stylistic commentary, but a production-facing description should make clear what is to be seen or heard.

**V.O.** commonly marks narration or another voice-over use. **O.S.** marks a character speaking from within the scene's location while outside the frame. If Ivo speaks from the doorway while the image remains on Maja, his speech can be marked O.S. A later narration commenting on this event would be a V.O. use. Phone dialogue is a case where script conventions vary. [Final Draft's explanation](https://www.finaldraft.com/blog/how-to-use-voice-over-in-a-screenplay-formatting-and-best-practices-explained) discusses the distinction and this variation.

### Speech need not resemble a formal report

“Without opening it?” is a fragment whose meaning is clear in context. Expanding it to “Are you instructing me to return the film can without opening it?” changes the rhythm and the relationship between the speakers. Grammatical analysis should explain what the line does before proposing a correction.

Dialogue may include contractions, interrupted sentences, repetition, hesitation and elliptical answers. These features can express character, pressure, uncertainty or conflict. Their value depends on the scene. An accidental ambiguity in a delivery email and an intentional ambiguity in dramatic dialogue require different editorial decisions.

Compare:

> **Explicit information:** “I am concerned that opening the can will reveal something I have concealed.”  
> **Indirect action:** “Put it back.”

The second line does not tell the reader exactly why Ivo objects. The surrounding action can make that uncertainty productive. When discussing dialogue, distinguish what is stated, what is implied and what you are inferring.

### Explain a line's function

A line can perform an action as well as convey information. It may request, refuse, accuse, reassure, evade or interrupt. Naming that action helps an English explanation remain precise.

| Wording | Possible function in context |
| --- | --- |
| “Did you check the label?” | A question, a reminder or an implied criticism. |
| “I said I would deal with it.” | A promise recalled or an attempt to end the discussion. |
| “You can leave it here.” | Permission, an offer of help or an instruction phrased indirectly. |
| “That is one way of describing it.” | Qualified agreement or scepticism. |

Intonation, timing, action and context help determine the reading. Avoid asserting a single emotional meaning from the isolated words alone. In an analysis, explain which evidence supports your interpretation.

### Distinguish dialogue, subtitles and captions

A transcript represents speech in written form. Subtitles are displayed in timed segments and must work with the moving image. Translation subtitles transfer dialogue into another language. Accessibility captions also convey relevant non-speech sound and speaker information. **SDH** means *subtitles for the deaf and hard of hearing*. The use of *captions* and *subtitles* varies between regions and services, so identify the intended audience and deliverable in the brief. The [W3C guidance on captions and subtitles](https://www.w3.org/WAI/media/av/captions/) explains this accessibility function.

For example, a translated line may tell a viewer what Maja says. If an unseen projector starting is important to understanding her reaction, an accessibility version may also need to convey that sound. A spoken-language transcript alone does not settle where or how the information should appear on screen.

**Audio description** supplies relevant visual information through an additional spoken description. It has a different purpose from captions for sound. The [W3C overview of accessible audiovisual media](https://www.w3.org/WAI/media/av/) distinguishes these services.

### Preserve meaning when shortening

Subtitling requires decisions about meaning, timing and readability. Shortening should preserve the action, the logical relationships and the speaker's degree of certainty.

Original line:

> If the archive confirms the date this afternoon, I can send you the revised credits tomorrow morning.

Possible condensed version:

> If the archive confirms the date this afternoon,  
> I can send the credits tomorrow morning.

This version preserves the condition and the proposed delivery. Whether omitting *revised* is acceptable depends on whether that distinction is already clear. If two credit versions are being discussed, it may be essential.

Misleading version:

> I will send the credits tomorrow morning.

This changes conditional ability into a commitment. Similar errors arise when a subtitle loses a negative, changes *might* to *will*, removes the person responsible or reveals information earlier than the speech does.

A useful revision sequence is to identify the essential meaning, remove dispensable wording, choose a natural formulation and check it against the scene. Word-for-word compression can preserve the vocabulary while damaging the meaning.

### Segment language into readable units

Line breaks should help a viewer follow the sentence. A break after a coherent phrase often reads more naturally than one that separates closely connected words.

Less helpful:

```text
Please send the revised
version before noon.
```

Clearer as a phrase division, if the available space permits:

```text
Please send the revised version
before noon.
```

The first division separates an adjective from the noun it modifies. The second keeps the noun phrase together. Line length, visual balance and timing still matter; phrase boundaries are a principle for judgement, not a mechanical answer to every case.

Do not impose one provider's requirements on every task. The [Netflix English (USA) Timed Text Style Guide](https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide) is an example of a specification for a named service and language variety. A different client may require a different subtitle type, character limit, reading rate, punctuation convention or delivery format. Use the specification that applies to the project.

### Understand the timing notation

SubRip, commonly identified by the extension **.srt**, represents a sequence of numbered cues. A cue gives start and end times, followed by its text; a blank line separates it from the next cue. Its timing notation uses hours, minutes, seconds and milliseconds. The [Library of Congress format description](https://www.loc.gov/preservation/digital/formats/fdd/fdd000569.shtml) documents this structure.

```text
1
00:00:12,000 --> 00:00:14,000
Keep the door open.

2
00:00:14,500 --> 00:00:16,500
I am bringing the projector in.
```

The first cue lasts two seconds and contains nineteen characters when spaces and punctuation are counted. For this example, define reading rate as visible characters divided by display duration: 19 ÷ 2 = **9.5 characters per second**. This is an arithmetic example, not a universal acceptable rate. A delivery specification must define the relevant limit and counting convention.

The comma before the final three digits marks milliseconds. It does not introduce a frame number. At 25 fps, one frame lasts 0.04 seconds, or 40 milliseconds; `00:00:12:10` in frame timecode therefore cannot be copied unchanged into SRT notation. Chapter 9 explains the distinction with an explicitly stated sequence origin.

For a classroom exercise, the brief might specify at most two lines, 37 characters per line and 15 characters per second, counting spaces and punctuation. Those figures belong to that exercise. Meeting them is only one part of success: the subtitle must also preserve the dialogue's meaning and fit its timing and context.

### Check subtitles against the audiovisual work

Check names, negatives, numbers, technical terms, speaker changes and the relationship between a cue and the event it accompanies. Automatic transcription or translation may produce plausible words that change the scene.

> **Spoken instruction:** “Do not remove the room tone.”  
> **Incorrect subtitle:** “Remove the room tone.”

The lost negative reverses the instruction. A spelling checker may find nothing wrong with the resulting sentence.

Reviewing the text as a document helps reveal language and consistency problems. Reviewing it with the image and sound is needed to assess timing, speaker reference and audiovisual meaning. In the exercises, the supplied dialogue, context and timing data define what can be checked; identify any judgement that would require seeing the actual scene.

## 14. Language in context

### Choose grammar to preserve the message

Grammar helps identify time, responsibility, certainty and relationships. In professional communication, a small change can alter an instruction or agreement. “You do not have to replace the shot” removes an obligation. “You must not replace the shot” prohibits the change.

This chapter brings together recurring patterns from the earlier chapters. Ceramella and Lee treat related language through production decisions, narrative, presentation and evaluation (2008, pp. 33–44, 64–65, 77–80, 83–85, 91–92). The examples below are original and concern film and television work.

### General work, current work and completed work

Use the **present simple** for regular activities, characteristics and an account of a finished work's content:

> She edits documentaries.  
> The scene begins with an empty corridor.  
> The final shot returns to the doorway.

Use the **present continuous** for work in progress or a temporary situation:

> She is editing a documentary about the archive.  
> We are testing two versions of the opening.

Use the **past simple** for an event located in a completed past period:

> We recorded the interview on Monday.  
> I sent the revised titles yesterday.

Use the **present perfect** to relate earlier work to the present without locating it in a finished past period:

> I have corrected the titles. The review copy is ready.  
> We have not received the approved spelling yet.

“I have sent it yesterday” combines a present-perfect form with a completed past-time expression. In this context, use “I sent it yesterday.” Both “I sent it” and “I have sent it” can report completion; the choice depends on the time frame and how the event relates to the current discussion.

The **past perfect** places an event before another past reference point:

> By the time the new credits arrived, I had exported the review copy.

This clarifies why that copy lacks the new credits. A sequence of past-perfect verbs is unnecessary once the ordering is clear; use the form where it helps the reader establish the relationship.

### Describe plans and commitments

Future reference has several useful forms:

| Form | Example | Typical use here |
| --- | --- | --- |
| Present continuous | “We are recording the interview on Thursday.” | An arrangement. |
| *Going to* | “I am going to compare the two endings.” | A plan or intention. |
| *Will* | “I will send the revised list by noon.” | A commitment in this context. |
| *Expect to* | “I expect to finish the revision this afternoon.” | An expectation, with less certainty than a promise. |
| *Be due to* | “The review is due to begin at ten.” | A scheduled or expected event. |

These forms overlap. Their interpretation depends on context; they are not labels that mechanically determine certainty. If a condition matters, state it: “I can finish the subtitles today if the dialogue remains unchanged.”

In an ordinary future time clause introduced by *when, after, before* or *as soon as*, use a present form:

> I will send the file as soon as I receive the approved titles.

The clause refers to the future without “as soon as I will receive.” By contrast, “Please confirm when you will send the titles” is an indirect question about a future time and can use *will*.

### Obligation, permission and uncertainty

| Expression | Meaning in the example |
| --- | --- |
| “The file must include the approved credits.” | A requirement. |
| “The file must not include temporary credits.” | A prohibition. |
| “You do not have to include subtitles in this test.” | Absence of obligation; inclusion is not automatically prohibited. |
| “You may use the smaller review file.” | Permission. |
| “The file may be incomplete.” | Possibility. |
| “You should check the names before export.” | A recommendation; a formal brief may define a stronger requirement. |
| “The difference might come from the playback settings.” | A tentative explanation. |
| “The editor can provide a shorter version.” | Ability or availability, depending on context. |

The same modal can perform different functions. Interpret it in the whole sentence. “It must be the older file” expresses a deduction, whereas “It must include the date” states a requirement.

For a past unnecessary action, distinguish:

> You need not have exported it again.  
> You did not need to export it again.

The first normally means that the export happened and was unnecessary. The second states that there was no need; the surrounding context establishes whether the person exported it anyway. If that distinction matters, add the fact explicitly.

### Conditions and consequences

Use a condition to identify what an action depends on:

> If the archive approves the names today, I will update the credits tomorrow.

The sentence does not say that approval is certain. *Provided that* makes the condition especially explicit:

> We can use the interview, provided that the factual information is checked.

*Unless* means approximately *if not* in this use:

> Keep the current opening unless the director approves the alternative.

The default is to keep the current opening. Avoid replacing this with “Change the opening unless…” because it reverses the practical instruction.

Use a more hypothetical form when considering an alternative:

> If we removed the final speech, the ending would depend more strongly on the image.

This is a proposal for thought or testing; it does not announce a decision. A past counterfactual concerns a situation that did not occur:

> If we had received the correct list earlier, we could have included it in yesterday's export.

The form connects a past condition with an unrealised possibility. It does not by itself establish blame. In professional correspondence, follow it with an actionable next step when one is needed.

### Active and passive: make responsibility clear

An active clause identifies the actor directly:

> The producer approved the revised schedule.

A passive clause puts the approved item first:

> The revised schedule was approved.

The passive is useful when the action or result matters more than the actor, or when the actor is unknown. It becomes unhelpful when a necessary responsibility disappears:

> The credits must be checked before delivery.

If this is a task assignment, say who will check them. “The production coordinator will check the credits before delivery” makes the responsibility explicit.

Do not use a passive to imply that an approval exists when it has only been requested. “Approval has been requested” and “The version has been approved” describe different states.

### Countable and uncountable nouns

Several common professional nouns are normally uncountable in the meanings used here:

| Use | Avoid in this meaning | A countable alternative |
| --- | --- | --- |
| some footage | three footages | three clips; footage from three takes |
| the equipment | several equipments | several items of equipment |
| useful information | useful informations | three pieces of information; three facts |
| practical advice | several advices | two suggestions; two pieces of advice |
| helpful feedback | many feedbacks | several comments; feedback on three versions |
| archive research | several researches | several studies, if these are separate investigations |

Use the singular verb with the uncountable noun: “The footage is ready.” Use the plural when the head noun is plural: “The clips are ready.” *Much* and *little* combine with uncountable quantities; *many* and *few* combine with countable plurals.

Some nouns change with meaning. “We need more light” concerns illumination; “We need two lights” concerns units or fixtures. “Sound is central to the scene” discusses an element of the work; “Three sounds overlap” identifies separate audible events.

### Articles and shared reference

Use **a/an** to introduce a member of a countable category without assuming that the reader already knows which member is intended. Use **the** when the intended reference is identifiable:

> We need a review copy. Please send the review copy you exported this morning.

“A director” refers to one member of the profession. “The director” normally identifies the director relevant to the current project or situation. A role can be introduced without claiming a particular production credit: “She works as an editor.”

The choice between *a* and *an* depends on the following sound: “an editor,” “a university production,” “an HD monitor.” A letter or word beginning with a vowel character does not automatically require *an*.

Demonstratives and pronouns also require a clear reference. After describing two versions, “It is too long” may be ambiguous. Name the version or component: “The opening of version 3 is too long for the requested duration.”

### Relative clauses and sentence attachment

A relative clause can identify which item is intended:

> Send the version that includes the approved credits.

It can also add information about an already identified item:

> Version 3, which includes the approved credits, is ready for review.

The first sentence distinguishes one version from others. The second adds information about version 3. Commas contribute to that distinction in writing.

Place a description near the word it modifies:

> Unclear: “I sent a note to the editor about the credits that was incomplete.”  
> Clearer: “I sent the editor an incomplete note about the credits.”

The first sentence delays the connection between *note* and *incomplete*. The revision makes it direct. If the credits were incomplete, use a different revision: “I sent the editor a note about the incomplete credits.”

### Link reasons, contrasts and purposes

| Relationship | Clause pattern | Noun-phrase pattern |
| --- | --- | --- |
| Reason | “We delayed the export because the names were unconfirmed.” | “We delayed the export because of the unconfirmed names.” |
| Contrast | “Although the opening is shorter, the order is unchanged.” | “Despite the shorter opening, the order is unchanged.” |
| Purpose | “We made a review copy so that the producer could check the titles.” | “We made a review copy for the title check.” |

*Because* introduces a clause; *because of* introduces a noun phrase. *Despite* can also take an *-ing* form: “Despite shortening the opening, we remained above the duration limit.” The understood subject of *shortening* is *we*.

Check that a participial opening connects to the intended actor:

> Misattached: “After checking the credits, the file was ready.”  
> Clearer: “After I checked the credits, the file was ready.”

The first construction grammatically attaches the checking to *the file*. The revision names the person who performed it.

Do not automatically use both *although* and *but* to introduce the same contrast: “Although the recording is quiet, the words remain clear” is complete.

### Use established word combinations

Meaning depends partly on collocation: the words that conventionally occur together. Learn an expression with its complement, not as an isolated translated verb.

| Useful expression | Example |
| --- | --- |
| responsible **for** | “She is responsible for the camera reports.” |
| focus **on** | “The revision focuses on the opening.” |
| depend **on** | “The export time depends on when the titles arrive.” |
| provide someone **with** something | “Please provide the editor with the revised list.” |
| explain something **to** someone | “Explain the change to the producer.” |
| discuss something | “We discussed the ending.” |
| agree **on** a decision | “We agreed on the shorter version.” |
| agree **to** an action | “I agreed to prepare another review copy.” |
| apologise **for** something | “I apologise for the incorrect attachment.” |
| comply **with** a requirement | “The file complies with the approved delivery brief.” |

Avoid “discuss about the ending” and “explain me the change” in these patterns. With suggestions, use “I suggest shortening the opening” or “I suggest that we shorten the opening.” With a request to a person, use “I asked the editor to shorten the opening.”

### Report speech and form indirect questions

Reported speech must preserve what was actually said. Reporting verbs encode different kinds of commitment:

> The director **suggested** removing the shot.  
> The director **agreed** to remove the shot.  
> The director **confirmed** that the shot had been removed.

A suggestion, agreement and confirmation are distinct events. Do not choose a stronger verb simply to make a summary shorter.

Use statement word order within an indirect question:

> Direct: “When will the titles arrive?”  
> Indirect: “Could you confirm when the titles will arrive?”

> Direct: “Does this include the subtitles?”  
> Indirect: “Please confirm whether this includes the subtitles.”

In “I do not know whether the file has been approved,” *whether* introduces an unresolved yes/no question. It does not mean the same as the conditional *if* in “I will send it if it has been approved,” although *if* can also introduce an indirect yes/no question in many contexts.

### State quantities and comparisons accurately

“We reduced the duration **from** 180 seconds **to** 150 seconds” gives the original and new values. “We reduced it **by** 30 seconds” gives the difference. Thirty seconds is one sixth of 180 seconds, so the reduction is approximately **16.7%** of the original duration.

Percentages and percentage points answer different questions. If the proportion of completed subtitles rises from 40% to 50%, it rises by **10 percentage points**. Relative to the initial 40%, the increase is **25%**, because 10 ÷ 40 = 0.25. State the reference quantity whenever confusion is possible.

Use comparable forms: “Version 3 is shorter **than** version 2”; “The opening is **as long as** the closing sequence”; “This shot is **less clearly focused than** the preceding shot.” Avoid a comparison that silently changes its basis, such as comparing one version's opening with another version's total duration.

### Make spoken English easy to follow

In an oral explanation, divide information into meaningful phrases and emphasise the words that distinguish the alternatives. “Fifteen frames” and “fifty frames” are very different instructions. If there is a risk of confusion, confirm the number in digits and give the unit: “Fifteen — one five — frames.”

Say what a number measures. *Twenty-five* could be a frame rate, a time, a file number or a quantity of takes. “Twenty-five frames per second” identifies the measurement. State dates with the month in words when regional number order might be ambiguous.

An effective presentation does not require an imitation of a particular accent. It requires intelligible words, manageable sentence lengths, accurate terms and a willingness to clarify. Pause before a key contrast, avoid speaking while looking away from the audience, and explain a technical abbreviation on first use when the listener may not know it.

### Revise in a useful order

Begin with meaning and facts: have you preserved the requirement, the degree of certainty and the person responsible? Then check organisation and paragraph purpose. Next check terminology, sentence structure and reference. Finish with spelling, punctuation, names, numbers and file/version labels.

A grammatically polished text can still be inaccurate. A technically correct text can still be hard to follow. A successful revision addresses both, and leaves you able to explain the final wording in your own words.

## 15. References

### Main book reference

Ceramella, Nick, and Elizabeth Lee. **2008. *Cambridge English for the Media*. Student's Book with Audio CD.** Cambridge University Press. ISBN 978-0-521-72457-9. [Publisher's bibliographic information](https://assets.cambridge.org/97805217/24579/frontmatter/9780521724579_frontmatter.pdf).

This book supports the connection between professional media vocabulary and reading, instructions, correspondence, project presentation and critical judgement. The following page ranges are particularly relevant. All numbers refer to the printed book.

| Topic | Pages |
| --- | --- |
| Briefing, instructions, clarification and feedback | 18–29 |
| Email register, professional briefs and narrative language | 33–41 |
| Television roles, filming schedules, location work and editing instructions | 42–51 |
| Film roles, screenplay, query letter, logline and pitch | 52–59; also 106 for logline and tagline |
| Film reviews and reasoned judgement | 61–62 |
| Definitions, problem descriptions, contextual meaning and collocation | 64–73 |
| Client communication, production planning and creative presentation | 74–83 |
| Numbers, press material and evaluation of results | 84–92 |

The professional scenarios, explanatory prose, model documents and exercises in this course material are original. The book is a supporting reference; its own tasks and recordings are separate resources. Current technical documentation supplements the book where terminology, software or delivery practices require a more specific account.

### Computers, digital media and cameras

The first four chapters cite technical sources beside the claims they support. The following groups indicate where to continue reading. Mathematical examples and schematics state their own assumptions; they do not substitute for the service manual or delivery specification of an actual device or production.

| Field | Primary references and their role |
| --- | --- |
| Computer circuits and architecture | MIT, [Computation Structures](https://computationstructures.org/): CMOS, logic, sequential state, processors and memory. Intel's [component terminology](https://www.intel.com/content/www/us/en/newsroom/tech101/explaining-common-chip-terms.html) and hardware documentation distinguish dies, packages, boards and connections. |
| Memory, storage and system software | Micron's [memory education material](https://www.micron.com/content/dam/micron/educatorhub/intro-to-memory/micron-intro-to-memory-presentation.pdf); [NVM Express specifications](https://nvmexpress.org/specifications/); [UEFI specification](https://uefi.org/specs/UEFI/2.11/); and [Linux memory documentation](https://docs.kernel.org/admin-guide/mm/concepts.html). |
| Units and character encoding | NIST's [binary-prefix definitions](https://physics.nist.gov/cuu/Units/binary.html) and the Unicode Consortium's [UTF encoding guidance](https://www.unicode.org/faq/utf_bom.html). |
| Audio conversion | Walt Kester's Analog Devices tutorials on [sampling](https://www.analog.com/media/en/training-seminars/tutorials/MT-002.pdf), [quantisation](https://www.analog.com/media/en/training-seminars/tutorials/MT-001.pdf), [successive approximation](https://www.analog.com/media/en/training-seminars/tutorials/MT-021.pdf) and [delta-sigma conversion](https://www.analog.com/media/en/training-seminars/tutorials/MT-022.pdf). |
| Digital sound history and coding | Sony's [history of the compact disc](https://www.sony.com/en/SonyInfo/CorporateInfo/History/SonyHistory/2-07.html); the shared CD physical-coding description in [ECMA-130](https://ecma-international.org/publications-and-standards/standards/ecma-130/); codec, container and preservation sources linked in the sound chapter. |
| Video signals and colour | ITU-R [BT.601](https://www.itu.int/rec/R-REC-BT.601/en), [BT.709](https://www.itu.int/rec/R-REC-BT.709/en), [BT.2020](https://www.itu.int/rec/R-REC-BT.2020/en) and [BT.2100](https://www.itu.int/rec/R-REC-BT.2100/en); EBU's [digital video level guidance](https://tech.ebu.ch/publications/r103). |
| Video compression and preservation | IETF/RFC documentation, codec specifications and manufacturer documentation linked in Chapter 3. Codec capabilities must be matched to the exact profile, precision and operating mode. |
| Image formation and exposure | Canon, Nikon, ZEISS and Edmund Optics documentation linked in Chapter 4 for focal length, entrance pupil, transmission, focus and diffraction. |
| Sensors and camera processing | Sony Semiconductor Solutions, Hamamatsu, Basler, ARRI, RED, Adobe and Blackmagic Design documentation linked in Chapter 4. Sensor architecture, exposure timing, raw processing and monitoring behaviour are tied to the documented implementation. |

### Professional terminology and documentation

Chapter 5 gives direct links next to the relevant groups of terms. The following overview identifies the main source organisations and their uses. A role profile describes a professional context; it should be read with attention to country, production type and the division of responsibilities. A manufacturer document explains a particular system or process and may change with its version.

| Source | Use in this material |
| --- | --- |
| **ScreenSkills.** Film and television job profiles and skills checklists; for example, [Director of photography](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/technical/director-of-photography-dop/), [Supervising sound editor](https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/post-production/supervising-sound-editor/) and [Vision mixer](https://www.screenskills.com/job-profiles/browse/unscripted-tv/editorial/vision-mixer/). | Departmental responsibilities, relationships between roles and variation in professional titles. The individual profiles used are linked throughout Chapter 5. |
| **Adobe.** Premiere and Media Encoder documentation; for example, [Slip edits](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-slip-edits.html), [EDL export](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-project-as-an-edl-file.html) and [Export settings](https://helpx.adobe.com/media-encoder/desktop/encoding-and-exporting/export-settings-reference.html). | Editing operations, interchange, compositing and delivery terminology. |
| **Avid.** [AAF format](https://kb.avid.com/pkb/articles/en_US/Knowledge/en336549). | Exchange of project information and media between applications. |
| **ARRI.** [Editorial workflow](https://www.arri.com/en/learn/camera-systems/pre-postproduction/editorial-workflow), [Visual-effects FAQ](https://www.arri.com/en/learn-help/learn-help-camera-system/image-science/vfx-faq) and technical documents linked in Chapter 5. | Camera and post-production relationships, image transforms and technical terminology. |
| **Nikon.** [Understanding maximum aperture](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/understanding-maximum-aperture) and [A basic look at exposure](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/a-basic-look-at-the-basics-of-exposure). **ZEISS.** [Zoom or prime lens?](https://lenspire.zeiss.com/photo/en/article/3-zoom-or-prime-lens-a-shootout-comparison/). | Optical and exposure distinctions used in explaining cinematography vocabulary. |
| **Blackmagic Design.** [ATEM Constellation: features](https://www.blackmagicdesign.com/products/atemconstellationip/features). | Examples of live-production terminology, including feeds and tally. |
| **Shure.** [Educational guide to audio systems](https://www.shure.com/en-US/docs/education/house-of-worship-audio-systems), especially microphone characteristics. | The distinction between sensitivity, noise and suitability for a recording situation; further sound sources are linked in Chapter 5. |
| **Final Draft.** [Glossary of Screenwriting Terms](https://kb.finaldraft.com/hc/en-us/articles/15575065049492-Glossary-of-Screenwriting-Terms). Hartman, Steven. 2026. [How to Use Voice Over in a Screenplay: Formatting and Best Practices Explained](https://www.finaldraft.com/blog/how-to-use-voice-over-in-a-screenplay-formatting-and-best-practices-explained). | Screenplay labels and the distinction between voice-over and off-screen scene dialogue. |

### Subtitles, accessibility and authentic project materials

**Library of Congress.** 2025. [SubRip Subtitle format (SRT)](https://www.loc.gov/preservation/digital/formats/fdd/fdd000569.shtml). Format description used for cue structure and timestamp notation.

**Netflix.** [English (USA) Timed Text Style Guide](https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide). An example of a provider-specific subtitle specification. The exercise limits in this material are explicitly supplied classroom conditions.

**World Wide Web Consortium, Web Accessibility Initiative.** 2024. [Captions/Subtitles](https://www.w3.org/WAI/media/av/captions/) and [Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/). Guidance used to distinguish captions, translation subtitles and audio description.

**Festival de Cannes.** [*La Chimera*: official film entry](https://www.festival-cannes.com/en/f/la-chimera/). An authentic example of a project entry with synopsis, credits and related publicity material.

Online sources were consulted for this edition on **7 October 2026**. For an actual production, check the current document and the brief that applies to that delivery.

### Citing this course material

Popič, Damjan. **2026. *English for Film and Television: Course materials / Učno gradivo*. Version 2.0.** [Version 2.0 source](https://github.com/damjan-popic/damjan-popic.github.io/blob/agrft-v2.0/content/en/teaching/agrft.md).

Use the version number when referring to this edition. The current course page may be revised; the archived version preserves the teaching text associated with this citation.

## 16. Exercises

Complete these exercises individually. Oral work consists of explaining, reading, presenting or responding to the lecturer. Calculation tasks specify their assumptions; practical observation uses the demonstrated equipment or the indicated schematic. State quantities, units and the limits of any inference.

The production, people, documents, source cards and dialogue in the professional exercises are fictional teaching examples. Their delivery and subtitle limits apply to the stated task. Answers follow all the exercise prompts; open tasks allow other defensible solutions.

### Computer exercises

Complete these tasks individually. Use the demonstration computer where indicated, and use the stated teaching models for calculations. A diagram of a representative machine cannot establish the wiring of a different motherboard.

#### H01. Identify the parts

Identify twelve parts on the opened computer or its documented component diagram. Include the motherboard, CPU package, cooler, memory module, storage device, PSU and three different connectors or interfaces. For each, give its English name, locate it and write one sentence explaining its function. If a part is hidden beneath a cover, distinguish what you can see from what you infer.

#### H02. Follow three connections

Use the computer-system schematic to trace three routes: a CPU access to main memory, a read from the illustrated NVMe SSD, and a transfer to a USB device through the chipset. Explain which routes share an upstream connection. Then explain why the actual machine's manual is needed before assigning its M.2 sockets to those routes.

#### H03. Separate power from information

A hypothetical circuit receives a constant 1.2 V and draws 5 A. Calculate its power. Its invented logic inputs recognise 0–0.3 V as 0 and 0.7–1.0 V as 1. Classify inputs of 0.2 V, 0.8 V and 0.5 V. Explain why these input levels do not determine the circuit's total power consumption. If voltage in the simplified switching-power model rises by 20%, with the other terms unchanged, by what percentage does that modelled contribution rise?

#### H04. Explain the inverter and NAND

For each inverter input state, identify which transistor conducts and which rail determines the settled output. Explain what happens while the input changes and why the ideal truth table does not describe every instant. Then derive the NAND result for A = 1, B = 0 from its series nMOS and parallel pMOS paths.

#### H05. Read the pattern

Convert 00101101 from binary to unsigned decimal and hexadecimal. Interpret 11111110 as an unsigned byte and as a signed two's-complement byte. Write the bytes of the sixteen-bit word 0x1234 in both byte orders. Explain why the character č cannot be represented by one ASCII byte.

#### H06. Trace an addition

Use the full-adder rules to calculate 23 + 11 as an eight-bit operation. Show each bit's carry input and output. Then compare the effects of 255 + 1 in unsigned eight-bit arithmetic and 127 + 1 in signed eight-bit arithmetic.

#### H07. Capture a state

An ideal positive-edge-triggered D flip-flop starts with Q = 0. At four successive valid rising edges, D is 1, 1, 0 and 1. Give Q after each edge. Between the second and third edges, D changes several times but meets all timing requirements at the third edge. Explain the effect on Q in the ideal model. State what setup time and hold time require in a real device.

#### H08. Compare memory mechanisms

Explain how a DRAM cell, a common SRAM cell, a NAND cell and an HDD retain recoverable information. Identify which ordinarily need power to retain the working state and which need refresh. Calculate how many distinct physical threshold states are needed for one, two, three and four encoded bits per NAND cell. Distinguish a cell from a byte.

#### H09. Distinguish capacity, addressing and speed

An invented machine is byte-addressable and has twelve address bits. What is its addressable capacity in bytes and KiB? Another system has a 16 GiB working-memory capacity and a 1 TB SSD. Explain why these two capacities cannot be added together and advertised as ordinary RAM. Define cache hit, cache miss, bandwidth and latency.

#### H10. Run the teaching processor

Use the ISA defined in the chapter. Replace the original program with bytes **10 17 20 0B 30 90 F0 00**, starting at address 0x00, with A = 0. Trace the accumulator, PC and changed memory location. State the complete eight-bit binary result. Explain how the result would differ if the operand 0B changed to 0A.

#### H11. Find the missing specification

For each statement, identify what remains unknown and write a precise follow-up question.

1. “The drive is M.2, so it must be NVMe.”
2. “It has USB-C, so it will be fast enough.”
3. “The slot is long enough, so all sixteen lanes are available.”
4. “The computer has a graphics card, so every video format has hardware decoding.”
5. “The camera cable fits the graphics card's HDMI socket, so we can capture the image.”

#### H12. Calculate a transfer

A 72 GB folder is copied at a constant useful rate of 180 MB/s. Calculate the transfer time. A network is described as 1 Gbit/s. Calculate its theoretical byte rate before overhead and the minimum time it could carry the same payload at that rate. Explain why a real copy can take longer even without a failed device.

#### H13. Follow a displayed frame

A working image buffer has 1280 × 720 pixels and four eight-bit components per pixel, tightly packed. Calculate its byte size and the traffic represented by reading 50 such buffers each second. In 120–180 words, explain why this buffer's rate can differ from the encoded file's bit rate, and identify at least four stages between SSD data and visible light.

#### H14. Choose a diagnostic test

A clip plays smoothly at normal speed, but scrubbing backwards is slow. The SSD has free space and the computer can play another clip smoothly. Give three technically plausible explanations and a test that could distinguish them. Separate observations from conclusions. Do not invent codec or hardware specifications that the prompt does not supply.

#### H15. Check the handover

Revise this report into an accurate, useful handover. Where the writer has not supplied evidence, ask for it instead of inventing a successful check.

> I converted the camera card into another folder and everything should be fine. The sizes looked similar. The project opens on my computer, so the files must be backed up. I will format the card now.

#### H16. Explain one complete mechanism

Prepare an individual explanation of approximately three minutes, supported by one of the schematics. Choose the CMOS inverter and adder, the teaching processor, or the route from a stored clip to picture and sound. Identify the input, internal stages, retained state, output and one limitation. Define five technical terms in context. Answer the lecturer's questions about the mechanism. This is practice; formal presentation requirements remain those announced for the course.

### Digital sound exercises

Work individually. Explain your reasoning in English. A calculation should name the quantity, show the units and end with a sentence interpreting the result.

#### A01. Explain the signal path

Follow the audio-chain schematic from a person speaking to sound coming from a loudspeaker. Write eight connected sentences explaining the stages. Use **converts, amplifies, samples, quantises, stores, decodes, reconstructs** and **drives** accurately. Identify where the signal is acoustic, analogue electrical and digital.

#### A02. Diagnose the stage

A microphone records a loud shout. The audio interface’s input stage overloads. The DAW’s channel fader is then lowered by 12 dB.

Explain whether this operation repairs the original recording. State which stage changed and what a different recording setup would need to prevent. Then explain why recording a floating-point file alone would not settle the question.

#### A03. Sample rate and aliasing

A mono recording uses a sample rate of 48 kHz.

1. Calculate the sample interval in microseconds.
2. State the Nyquist frequency.
3. An unfiltered 31 kHz cosine enters an ideal sampler. Find the frequency of the corresponding alias between 0 and 24 kHz.
4. Explain why a filter applied after sampling cannot reliably separate that alias from a genuine input component at the same frequency.
5. Explain why stereo recording does not double the stated sample rate.

#### A04. Read the bytes

One stereo sample frame contains left = +513 and right = −513. Use signed 16-bit two’s complement and left-first interleaving.

1. Express both values as four-digit hexadecimal words.
2. Write the four stored bytes in little-endian order.
3. Write them in big-endian order.
4. Explain whether correct conversion between these byte orders changes the intended sound.
5. State what additional information you need to interpret a long raw byte stream.

#### A05. A converter’s decisions

Use the chapter’s simplified four-bit successive-approximation model: reference = 1 V; code `k` represents `k/16` volts; lower-edge decisions.

For a held input of 0.43 V, show the four trial codes, comparator decisions and final code. State the represented voltage. Explain why your result uses a different quantisation convention from rounding to the nearest permitted level.

#### A06. Plan the recording capacity

A fictional session records six channels for 30 minutes at 48 kHz, 24-bit integer PCM. Each sample occupies three bytes.

Calculate:

1. The PCM bit rate.
2. The byte rate.
3. The audio payload for the full recording, in bytes and decimal GB.
4. The effect of doubling the duration.
5. The effect of using 96 kHz instead, keeping the other settings unchanged.

Explain why the payload calculation is not a guarantee of the exact file size or all the storage needed for the production.

#### A07. Buffers and monitoring

Compare buffers of 128 and 512 sample frames at 48 kHz. Calculate each buffer’s duration in milliseconds. Explain one benefit and one cost of using the larger buffer.

A colleague says: “The buffer is 128 samples, so the complete round-trip latency is exactly 2.67 milliseconds.” Correct the statement.

#### A08. Dither, noise and precision

For each statement, write **accurate**, **inaccurate**, or **needs a condition**, then supply the missing explanation.

1. Increasing bit depth increases the number of sample instants.
2. A recorder with 24-bit output necessarily measures 24 bits of useful signal.
3. Dither can make the error from bit-depth reduction less signal-dependent.
4. A fresh dither pass is needed whenever an unchanged integer PCM file is copied.
5. A signal below one LSB must always be represented as permanent silence.
6. A larger floating-point range prevents all analogue overload.

#### A09. Read an audio CD precisely

Using the chapter’s CD schematic, calculate the following for one second of standard audio-CD playback:

1. The number of stereo sample frames.
2. The PCM audio payload in bytes and bits.
3. The number of 2,352-byte audio blocks.
4. The number of small CD channel frames.
5. The physical channel-bit rate using 588 channel bits per small frame.

Explain why the PCM rate and the physical channel rate differ. Correct the sentence: “Each pit on the disc is one bit of the original PCM recording.”

#### A10. Encode and decode a lossless prediction

The original signed integer samples are:

`200, 203, 205, 204, 204, 201`

Predict each sample from the preceding sample. Store the first value and calculate the five residuals. Reconstruct the sequence to prove that nothing has been lost.

For a toy code, use 16 bits for the first value and four bits for each residual. Compare the payload size with storing all six samples independently as 16-bit words. State two qualifications needed before claiming that a real file will have exactly that compression ratio.

#### A11. Describe a file without guessing

A fictional inspection report gives:

| Field | Value |
| --- | --- |
| Filename | `SC07_TK03.wav` |
| Container | WAVE with production metadata |
| Encoding | 24-bit signed integer PCM |
| Sample rate | 48,000 Hz |
| Channels | Four |
| Track labels | Boom; Radio A; Radio B; Production mix |

Write a five-sentence description. Explain what the extension alone would not have told you. State whether the four channels must be described as a stereo or surround mix.

Then classify **FLAC, AAC, BWF, Opus, MIDI** and **USB** by their roles.

#### A12. Trace a lossy generation

Begin with an original integer PCM master. It is encoded to MP3. The MP3 is decoded to a specified 16-bit PCM sequence, which is then encoded losslessly to FLAC and later decoded back to 16-bit PCM with no further processing.

Which sample sequence must the final PCM match? Which earlier sequence is it not guaranteed to match? Explain why neither a larger WAVE file nor a higher nominal sample rate proves that the original information has been recovered.

#### A13. Separate four meanings of level

A file has an integrated loudness reading of −23 LUFS and a reported true peak of −1 dBTP. During playback, the listener turns down the loudspeaker amplifier.

Explain what happens to the file’s stored data and what happens to the acoustic level in the room. Does the information establish a particular dB SPL? Does it establish compliance with every possible delivery specification?

Then add two aligned floating-point sample values, 0.8 and 0.6. Apply a gain of 0.5 to their sum. Explain the difference between retaining that sum in floating point and clipping it to an integer full-scale limit before reducing the gain.

#### A14. Find the timing problem

Two devices begin aligned. After one hour, their recordings differ by 180 milliseconds.

1. Calculate the approximate relative rate difference in parts per million.
2. Express the offset in frames at exactly 25 fps.
3. Explain why a correct initial timecode label does not rule out clock drift.
4. State the distinct roles of timecode and word clock.
5. A separate one-second clip containing 44,100 sample frames is incorrectly played at 48 kHz without resampling. Calculate its new duration.

#### A15. Write the technical handover

Write 180–230 words handing a fictional recording to an assistant editor. Use these facts:

- Four isolated microphone tracks and one production mix were recorded.
- All files contain 48 kHz, 24-bit integer PCM with BWF metadata.
- The project uses exactly 25 fps.
- The clap aligns at the start of the first take; the end has not yet been checked.
- Original recordings are preserved.
- A smaller AAC review copy will be made from the agreed master.
- One take contains a distorted shout whose cause has not yet been established.

Identify what is known, what needs checking and what the review copy is for. Avoid unsupported claims such as “perfectly synchronised”, “lossless from microphone to listener” or “the distortion can definitely be repaired”.

### Video exercises

These tasks are individual. Use complete technical explanations when a question asks how or why; a term alone is insufficient. Calculations use decimal MB and GB, and active-picture payloads exclude sound, metadata and padding unless stated.

#### V01. Trace an analogue capture

An archive has a VHS cassette and a computer with a capture interface. Write a functional chain from tape to file. Explain the jobs of the playback deck, time-base correction, colour decoding, analogue-to-digital conversion and file creation. Identify two things that making a 3840 × 2160 capture file cannot restore.

#### V02. Read the line waveform

Using the analogue-line schematic, identify the sync pulse, back porch, colour burst, active video and front porch. For a 625-line, 25-frame-per-second system, calculate the line rate and line duration. Then calculate how long 720 luma sample periods last at 13.5 MHz. Explain why a complete line and a digital active line have different lengths.

#### V03. Explain the fields

A genuinely interlaced recording contains 50 fields per second. Field A shows a moving edge at horizontal position 100; the next field B shows it at position 110. Explain what a simple weave will show. State the field interval and field-pair rate. Compare discarding one field with producing one reconstructed progressive picture per field. Explain why PsF requires different reasoning.

#### V04. Read the bits

An uncompressed RGB pixel has eight-bit component values R′ = 64, G′ = 128 and B′ = 255. Write each as an eight-bit binary word and calculate the total number of bits. State the number of possible codes and maximum unsigned code for ten-bit and twelve-bit components. Explain why these numbers do not establish the pixel’s physical colour without further information.

#### V05. Calculate a colour-difference representation

Use the BT.709 equations in the chapter for R′ = 0, G′ = 0, B′ = 1. Calculate normalised Y′, Cb and Cr. Then use:

`Ycode = round(16 + 219Y′)`

`Cbcode = round(128 + 224Cb)`

`Crcode = round(128 + 224Cr)`

Give the resulting eight-bit narrow-range codes. Explain why negative normalised Cr is not an invalid value, and why changing a matrix tag is not necessarily a colour conversion.

#### V06. Count what is retained

A progressive image is 6 × 4 luma samples. Count Y′, Cb and Cr samples in 4:4:4, 4:2:2 and 4:2:0. Calculate the nominal bits for each representation at ten bits per component sample. Explain what interpolation can and cannot do when the 4:2:0 version is converted to 4:4:4. Do not assume one universal chroma-siting convention.

#### V07. Plan the data rate

Calculate the active-picture payload for 1920 × 1080p50, ten-bit 4:2:2 video, in bit/s, decimal MB/s and decimal GB for ten minutes. A compressed viewing version averages 16 Mbit/s for the same ten minutes. Calculate its video payload size. Give three reasons why neither number is automatically the exact final file size.

#### V08. Find the lossy step

A prediction has samples 100, 100, 100 and 100. The original samples are 101, 103, 108 and 109. Calculate the residual. For a separate transform example, quantise coefficients 19, 5 and −7 using a step of 8 and nearest-integer rounding, then reconstruct them. Identify the irreversible step. Explain why entropy decoding can recover the quantised coefficients exactly without recovering the original coefficients.

#### V09. Decode a GOP

Use the example I0, B1, B2, P3 in display order. State one valid decoding order and explain its dependency logic. Which pictures in this example depend on P3? Explain why the sentence “B-frames are never used as references” is too broad. Distinguish an I picture from a guaranteed clean random-access point.

#### V10. Diagnose the handover

Two files both end in `.mp4` and have 3840 × 2160 pictures. File A is eight-bit 4:2:0 AVC at 25 fps. File B is ten-bit 4:2:2 HEVC at 50 fps. The editor can play A smoothly but struggles with B.

Write a short technical reply explaining why the shared extension and dimensions do not guarantee the same performance. Name five properties to check. Explain when rewrapping could help and when an editing transcode or proxy would address a different problem. Do not assume that the latest codec or the largest file must be best.

#### V11. Separate colour problems

For each case, state the first interpretation to investigate and one check you would make.

1. Nominal black in a narrow-range file appears grey in one player.
2. Log footage looks flat when opened directly on an SDR display.
3. A PQ file becomes excessively dark after somebody only changes its tag to Rec.709.
4. A ten-bit export still shows the same banded gradient as an eight-bit source.

Write one sentence distinguishing UHD, wide colour gamut and HDR.

#### V12. Time, sync and the master

At 25 fps, calculate the duration from in-point `01:02:14:08` to exclusive out-point `01:02:18:16`. Write the next valid 29.97 drop-frame label after `00:00:59;29` and after `00:09:59;29`. Explain whether any pictures were removed.

Finally, write a 100–140-word handover note for an analogue capture. Distinguish the preservation master, an editing representation if needed, and a viewing copy. Mention field order, colour interpretation, audio, verification and retained source identification. Treat the format choice as a reasoned proposal rather than a universal preservation rule.

### Camera exercises

Complete these exercises individually. Use full English sentences for explanations, state the assumptions behind calculations, and include units. A technically correct answer should explain a mechanism or a consequence as well as naming a term.

#### C01. Name, locate and explain

Choose eight visible parts of the camera demonstrated in class. Include the lens mount, focus control, aperture control, recording medium and one connection. For each part, write three sentences: identify it, locate it, and explain its function. If a part is absent, identify the equivalent function in the demonstrated system. Add a fourth sentence explaining one distinction that matters: for example, focus versus zoom, or timecode versus genlock.

#### C02. Draw and calculate an image

Use an ideal thin lens with f = 75 mm. An object is 600 mm from the lens plane and 120 mm high.

1. Calculate image distance and magnification.
2. Calculate image height, including its sign.
3. Draw the optical axis, lens plane, two focal points, object and image.
4. Construct two rays from the object tip that meet at the image tip.
5. Explain why the calculated image distance is not automatically the flange focal distance of a real camera.

#### C03. Focal length, crop and perspective

A rectilinear 35 mm lens is focused at infinity. Camera mode A uses an active width of 36 mm; mode B uses 24 mm.

1. Calculate the horizontal angle of view in each mode.
2. State whether the lens's focal length changes when the camera switches modes.
3. Explain whether perspective changes when the camera remains fixed.
4. Explain what can change if the operator moves the camera backwards to recover the original size of a nearby subject in mode B.

#### C04. Keep exposure while changing the picture

A shot is correctly exposed at f/5.6, 1/50 s, with ND 0.6. The sensor operating mode, lighting and framing remain unchanged. The new creative choice is f/2.8 and 1/100 s.

1. Calculate the separate stop changes from aperture and exposure time using conventional full-stop labels.
2. Calculate the net exposure change before changing ND.
3. Select the new conventional ND density needed to restore the original exposure.
4. Explain two image characteristics that may differ even when total sensor exposure is restored.

#### C05. f-number and transmission

Lens A is set to f/2 and transmits a fraction τ = 0.64 of the relevant light. In this simplified model, lens B has perfect transmission.

1. Calculate the T-number of lens A.
2. Find the f-number at which lens B provides matching exposure under unchanged conditions.
3. Explain why the result does not establish identical depth of field or rendering.
4. A filter is labelled ND8. Explain the common meaning of this notation and why it must not be confused with optical density 8.

#### C06. Correct the mechanism

Rewrite each statement accurately. Add a short explanation.

1. “The sensor converts each photon directly into a zero or a one.”
2. “A CCD camera is analogue; a CMOS camera is digital.”
3. “Every site of a Bayer sensor directly measures red, green and blue.”
4. “Every CMOS sensor has rolling shutter.”
5. “The aperture is the number written on the iris ring.”

#### C07. From photons to a binary code

Use the invented model from the reading: quantum efficiency 0.5; conversion 100 μV per electron after reference-offset removal; ideal 10-bit ADC spanning 0–1.024 V in 1 mV bins; code = floor(voltage/0.001 V), clipped to 0–1,023.

The exposure delivers a mean of 6,000 photons to the detector.

1. Calculate mean detected electrons, expected voltage and digital code.
2. Write the code using ten binary digits and check its decimal value.
3. Estimate photon-limited noise in electrons and ADC codes using the square-root model.
4. Explain why increasing the file's nominal bit depth would not remove that photon noise.

#### C08. Read the timing diagram

Four illustrative sensor rows start exposure at 0, 5, 10 and 15 ms. Each exposes for 8 ms. The next frame's first row starts at 40 ms.

1. Write each row's exposure-end time.
2. Calculate the frame rate, row exposure duration and first-to-last start skew.
3. Explain why a rapidly moving vertical feature may appear tilted.
4. Describe what would change if every row instead exposed from 0 to 8 ms.
5. Explain why simultaneous exposure does not require every pixel's data to leave the camera simultaneously.

#### C09. Capture speed and playback speed

A camera records two seconds of action at exactly 100 fps. The edit interprets all captured frames at exactly 25 fps without dropping or duplicating them.

1. Calculate the number of captured frames and playback duration.
2. Calculate exposure time for a 180° shutter at the capture rate.
3. Compare motion blur with an otherwise equivalent 25 fps, 180° recording.
4. Explain why the two-second real-time audio cannot simply remain unchanged in duration and stay synchronized with the eight-second presentation.

#### C10. Explain raw, log, LUT and ISO

Write 150–200 words correcting this camera report:

> We recorded raw, so nothing was processed. Log is the compression format. Raising ISO made the sensor collect more photons. We used a LUT, so the recorded file must contain that look. White balance can always be fixed perfectly later.

Your corrected report must distinguish a general principle from a behaviour that requires checking the camera's recording mode or format documentation.

#### C11. Diagnose without guessing

Write a short investigation plan for each observation. Include an initial hypothesis, one controlled check, and one alternative cause or limitation.

1. Fine costume fabric shows moving coloured patterns.
2. Horizontal bands appear when a particular LED is dimmed.
3. The monitor looks correctly exposed, but the editor sees an unexpectedly dark image.
4. A face is soft while the chair behind it is sharp.
5. A card has free space, but the camera stops during a long take.

Use conditional language where the evidence is incomplete. Do not present a possible cause as a confirmed fault.

#### C12. Prepare the handover

For an original classroom shot, the agreed recording is progressive 25 fps with sixty seconds of constant video payload at 100 Mbit/s and one uncompressed 48 kHz, 24-bit audio channel. Ignore overhead for the calculation.

1. Calculate video bytes, audio bytes, combined decimal megabytes and captured frames.
2. Write a concise camera report specifying recording mode, frame rate, exposure time or shutter angle, lens and focus information, white balance, colour encoding, monitoring LUT status, clip/take identification and useful sound information. Supply plausible proposed values where the brief leaves a field open, and label those as your choices.
3. Describe the route from light entering the lens to the editor opening the verified copy in 120–180 words.
4. Name one decision belonging to photographic practice, one to camera operation, and one to media handling. Explain how responsibilities should be confirmed when the production has a small crew.

### People, professions, and terminology

#### E04. Identify the professional responsibility

Use the responsibilities in this fictional production note. Titles and duties can differ between productions.

| Role | Responsibility on this production |
|---|---|
| Director | Interprets the script and guides performances and the scene's dramatic treatment. |
| Cinematographer / director of photography | Plans the photographic approach with the director and leads its implementation. |
| First assistant camera | Manages focus during takes and supports the camera's preparation. |
| Second assistant camera | Operates the slate and maintains the camera reports. |
| Gaffer | Leads the lighting crew in implementing the agreed lighting plan. |
| Production sound mixer | Oversees location sound recording. |
| Editor | Selects and arranges picture and sound material to construct the film. |
| Sound editor | Prepares and edits sound material in post-production. |
| Producer | Oversees the production's organisation, resources, and delivery. |
| Location manager | Arranges and coordinates the use of locations. |

Identify the first relevant contact for: (a) an actor's motivation; (b) a missing camera-report entry; (c) the intended photographic contrast; (d) building access; (e) a focus change during a take; (f) location dialogue recording; (g) funding an additional filming day; (h) implementing the lighting plan; (i) restructuring the opening; (j) organising post-production sound elements. Give the role and a reason in a complete sentence.

#### E05. Explain your department to another profession

Choose directing, cinematography, or editing. Write 120–150 words explaining what information your department needs from the other two departments **on the fictional production in E04**. Give two concrete examples of an unclear handover and explain how to improve them.

Use five professional terms, explaining essential ones. Distinguish your responsibility from a decision requiring another person's input.

#### E06. Shot, take, set-up, scene, or sequence?

Use each term appropriately. Some terms may be used more than once.

1. The actors perform the same planned shot for the fourth time. It is the fourth ______.
2. An uninterrupted image runs from one cut to the next in the finished edit. It is a ______.
3. The crew changes the camera position and lighting arrangement before recording the next angle. They prepare a new ______.
4. A stretch of action takes place in the cinema foyer during the evening. In the script it is numbered as a ______.
5. Several connected scenes show the search for a missing reel. Together they form a narrative ______.
6. “We need another shot” could mean another recording, another camera view, or additional coverage. Rewrite the request so that it clearly asks for a repeat of the same performance and camera arrangement.

#### E07. Distinguish staging, framing, and editing

Choose the most precise term for each description: **blocking, framing, coverage, continuity, eyeline match, montage**. Then explain why a different term from the list would not fit as well.

1. The director decides when Maja crosses the foyer and where Ivo stands.
2. The camera view includes the door but excludes the noticeboard beside it.
3. The production records additional angles and reactions that will give the editor options.
4. A cup changes position between views without an action explaining the change.
5. A character looks off screen; the next shot presents the object of that look.
6. A series of brief images compresses several evenings of preparation into twenty seconds.

For item 6, discuss the intended function; short shots can serve different purposes.

#### E08. Remove spatial ambiguity

Rewrite the following notes using explicit reference points. You may name a person or object and specify “in the image,” “from the camera's viewpoint,” or “from the performer's viewpoint.”

1. “Move left.” Intended meaning: Maja should appear nearer the left edge of the recorded image.
2. “Put it behind him.” Intended meaning: the noticeboard should be beyond Ivo, farther from the camera.
3. “Look over there.” Intended meaning: Maja should look at the empty seat beside the doorway.
4. “Use the other side.” Intended meaning: use the recorded angle looking from the doorway towards the counter.

Add one clarification question for a case in which the intended meaning is unknown.

#### E09. Diagnose imprecise camera language

Identify the distinction being confused and rewrite each note. Use the information in parentheses.

1. “Use a close-up lens.” (The desired result is a frame showing Maja's face, not a specified focal length.)
2. “The exposure is out of focus.” (Focus falls behind Maja, leaving her face soft; the image brightness is acceptable.)
3. “The lens has a very wide depth of field.” (Objects at many different distances appear acceptably sharp.)
4. “Pan forward towards the actor.” (The request concerns moving the camera closer, not turning it horizontally from a fixed position.)
5. “Make the background wider.” (The request is to include more of the surroundings in the frame.)

For item 5, clarify the intention before proposing a technical solution.

#### E10. Read a post-production plan

The producer has approved this simplified plan:

> First, the editor assembles the available scenes. The team then revises structure, duration, and individual cut points. When the picture edit has been approved and designated as locked, sound and colour work proceed against that version. The finishing team checks that the material used for finishing corresponds to the approved edit. Any later picture change must be reported and its consequences agreed.

Explain **assembly, rough cut, fine cut, picture lock, conform, colour grade,** and **final mix** in this context. Which stages may involve changes to shot order? Why would changing a shot after picture lock affect other departments? Explain why an “approved cut” does not necessarily mean that every delivery file has already been completed.

#### E11. Repair misleading translations

Rewrite these sentences in natural professional English. Preserve the intended meaning in parentheses.

1. “I realised a documentary last year.” (The student directed it.)
2. “This is the actual version.” (It is the most recent working version.)
3. “Please control the names in the credits.” (Check their spelling.)
4. “We need a sensible microphone.” (It must detect a quiet sound reliably; no purchase recommendation is required.)
5. “The montage begins on Monday.” (The process of editing the whole film begins.)
6. “Please record the file in the shared folder.” (Save an existing file there.)

Explain why familiar-looking English words can convey the wrong professional meaning.

### On set and in the studio

#### E18. Give an actionable instruction

Rewrite each message so that it identifies an action and a way to confirm completion.

1. “Someone should sort out the paperwork.” The producer wants the assistant to email shot list v03 to the director before 16:00.
2. “The sound is bad.” Audible ventilation continues beneath the dialogue in take 2; the sound department needs to assess that recording.
3. “Do the same again.” Repeat take 3's dialogue and blocking, but record the revised framing in the approved shot list.
4. “Everybody knows what to do.” The editor has not received the revised scene order.

Use requests appropriate to a colleague and your own authority.

#### E19. Report the problem you can observe

A review copy contains a brief black image at the join between shots 4B and 4D. It occurs in the exported review file and can be reproduced at the same position. You have not checked the editing project, original recordings, or export settings.

Write an 80–100-word issue report. Separate the symptom from a possible cause. Name the material, describe reproducibility, and request a check. Use a clearly marked placeholder such as “[exact timecode to be confirmed]” rather than inventing a measurement. Explain why “The camera failed” is not justified by the evidence supplied.

#### E20. Confirm a change and its limits

The producer sends this fictional update:

> The foyer remains available from 09:00 to 12:00. Ivo's performer will arrive at 10:00. Maja's performer is available from 08:30. Shots involving both performers must therefore be scheduled after 10:00. The projection room is still unconfirmed. Do not add a second filming day without asking me.

Write a reply of 80–110 words confirming a workable order for the morning. Include one question about the unconfirmed part of the plan. Identify what can proceed and what depends on further information. Do not promise that all footage will be completed by noon; the brief does not establish that.

#### E21. Read back exact information

Prepare a 45–60-second individual confirmation for the instructor using these exercise requirements:

| Item | Required information |
|---|---|
| Current shot list | Version 3, dated 15 October 2026 |
| Crew arrival | 08:45 |
| First recording | 09:15 |
| Review file | 1920 × 1080 pixels; 25 frames per second |
| Reference point for an issue | Timeline timecode 01:02:14:08; 25 fps, non-drop-frame |

Distinguish dimensions, frame rate, and timecode. Read the timecode as hours, minutes, seconds, and frames, or identify that convention before reading the numbers. The instructor may ask you to repeat one item or distinguish it from another. Accuracy matters more than speed.

### Working in English

#### E01. Explain what you do

Write a professional introduction of 90–120 words. Use your own experience or this fictional profile:

> Alex is a second-year cinematography student. Alex has shot two short student films, enjoys working with available light, and is interested in how framing directs attention. Alex has operated a camera but has not led a professional camera department. Alex wants to become more confident when discussing visual choices in English.

State your field, experience, one interest, and a learning aim. Distinguish “I have worked as…” from “I would like to work as…”. Prepare to explain the information briefly to the instructor without reading it word for word.

#### E02. Replace vague language

Rewrite this introduction in 60–90 words. Preserve its modest level of experience and replace general claims with information from the fact list.

> I do all the camera things and I am really professional. I made many things and they were very good. I want to realise films and control everything better.

Facts: the student operated the camera on two three-minute exercises; another student designed the lighting; one exercise used a fixed camera and the other used a moving camera; the student now wants to explain camera movement and framing more precisely. Do not invent awards, professional employment, or expertise in every department.

#### E03. Ask a useful question

Write one clarification question and one conditional confirmation for each instruction:

1. “Send the final version tomorrow.” The version, time, and recipient are unspecified.
2. “Make the opening tighter.” It is unclear whether this concerns duration, shot size, or pacing.
3. “We need a clean version.” It is unclear what should be removed or retained.

A conditional confirmation states what you will do **if** your interpretation is confirmed. Use at least two different question openings.

### Reading, listening, and checking sources

#### E12. Read a production brief

Read the original brief, then answer the questions below.

> **The Last Showing** is a seven-minute fictional short set in a small cinema during its final week. Maja, a trainee projectionist, discovers that the ending of a local amateur film is missing. She asks Ivo, a former projectionist, to help reconstruct what happened. The story uses two speaking characters, six audience extras, a foyer, and a projection room. The director wants the film to feel restrained rather than nostalgic. One test scene has already been recorded; its dialogue can be understood, but a ventilation noise is audible throughout. The production has permission to use the two rooms on one agreed day. A new arrangement would be needed for any return visit. The final delivery date and file specifications have not yet been confirmed.

List five confirmed facts and three decisions still needed. Distinguish a story requirement, a production constraint, an aesthetic intention, and an observed technical problem. Write a two-sentence summary for an editor who has not seen the brief. Do not claim that the film has been shot or that the sound problem has already been solved.

#### E13. Separate observation from interpretation

Analyse this original review note:

> The opening begins with three static shots and no dialogue. Each of these shots lasts approximately eight seconds. The repeated empty spaces suggest that the building has outlived its audience. For me, the rhythm becomes less effective when a fourth similar shot follows. I would test the opening without that shot before changing the rest of the sequence.

Identify: (a) two observations; (b) an interpretation; (c) a qualified evaluation; (d) a proposed action. Which claims could be checked directly against the edit? Which depend on an interpretation or judgement? Rewrite the evaluation for a formal report without pretending that it is a measurable fact.

#### E14. Choose a source for the question

These source cards are invented for this exercise.

| Source | Information available |
|---|---|
| A. Producer's delivery brief, approved yesterday | Required files for this particular project and the named person who approves them. |
| B. Manufacturer's manual for the camera model used | Controls, supported recording options, and model-specific terminology. |
| C. A 2011 forum discussion | Several users' experiences with a different camera model. |
| D. A current professional role profile | Typical responsibilities and variation within a named occupation. |
| E. A festival's current submission page | Submission-stage requirements and a warning that selected films receive separate screening instructions. |
| F. An anonymous search-result summary | A short statement with no accessible author, date, or supporting document. |

Choose the best starting source for: this project's final files; this camera's recording options; the usual role of a focus puller; and the festival's initial submission. Explain why a source can be reliable yet irrelevant to a particular decision. Which question cannot be answered fully from E alone?

#### E15. Resolve an apparent contradiction

Compare these fictional messages:

> **Message A, editor, Monday 09:10:** “The review export is 1280 × 720. It is intended for comments on content and timing.”
>
> **Message B, producer, Monday 11:30:** “The final picture file must be 1920 × 1080. Please wait for the approved delivery brief before exporting the final files.”
>
> **Message C, assistant, Monday 12:00:** “I found the review copy, so the film's required delivery resolution is 1280 × 720.”

Explain whether A and B contradict each other. Identify C's unsupported inference. Write a correction of 60–80 words that names the relevant document, distinguishes the purposes of the files, and requests the missing specification without accusing the assistant of incompetence.

#### E16. Listen to a changed plan

The instructor reads this original text twice. First identify the change; then note times, responsibilities, and uncertainty. Keep the transcript covered during listening. It is included for independent study.

> Tomorrow's session will start in the foyer at nine fifteen, not nine. Please arrive by eight forty-five so that we can check the documents first. We will record Maja's entrance before the conversation with Ivo because Ivo's performer cannot arrive before ten. The conversation is still planned for the foyer. The producer will confirm this afternoon whether the projection room is available after lunch. Do not treat that room as confirmed yet. Bring the revised shot list, version three, and keep version two for reference. Send any questions about the plan to the producer before four this afternoon.

Answer individually: What is the session start? What is the arrival time? Why has the order changed? Which location remains uncertain? Which shot-list version is current? Who receives questions, and by when? Finish with a spoken or written confirmation of no more than four sentences. Do not interpret “not confirmed” as “cancelled.”

#### E17. Build a useful terminology record

Use these short teaching definitions:

> **Coverage:** the views and performances recorded to provide material for constructing a scene in the edit. **Continuity:** consistency of relevant details or relationships across recordings or edited images. **Room tone:** a recording of a location's background sound under the relevant recording conditions. **Picture lock:** an agreed status of the picture edit after which further picture changes require explicit coordination.

For each term, record its English form, a concise explanation in your own words, one useful collocation, and an original sentence connected to *The Last Showing*. Add a Slovenian equivalent or explanatory phrase if it helps you. Identify the source as “Exercise E17, teaching definition”; do not attribute it to a dictionary you have not consulted. Mark any translation you still need to verify.

### Production documents

#### E22. Read a simplified call sheet

This fictional call sheet contains only the information needed for the language task.

| Field | Entry |
|---|---|
| Production | *The Last Showing* |
| Date and time zone | Thursday 15 October 2026; all times local to Ljubljana |
| Location | Fictional Aurora Cinema, foyer |
| Crew call | 08:00 |
| Performers' call | Maja 08:30; Ivo 08:30 |
| Scene 4 | Conversation between Maja and Ivo; recording planned 09:15–10:30 |
| Scene 5 | Maja alone; recording planned 10:45–12:00 |
| Meal break | 12:30 |
| Current document | Call sheet v02, issued at 18:00 on 14 October |

A later message says: “Ivo can arrive only at 10:00. The producer is revising the morning order.” Identify the conflict. Which entries need confirmation? Why should the editor not silently alter and redistribute the call sheet? Write a 50–70-word request for the updated document. Treat this exercise independently of the times in E20–E21.

#### E23. Interpret a shot list

Read this simplified list for scene 4. “Static” means that no camera movement is planned for these entries.

| Shot | Framing and action | Sound / continuity note |
|---|---|---|
| 4A | Medium two-shot: Maja asks Ivo about the missing ending. Static. | Record complete dialogue. Maja holds the envelope. |
| 4B | Close-up of Maja as she opens the envelope. Static. | Her look towards Ivo follows the opening action. |
| 4C | Insert of the envelope label. Static. | The label must match the prop visible in 4A and 4B. |
| 4D | Close-up of Ivo before he answers. Static. | Retain a short pause before the first word. |

What does 4C contribute that 4A may not show clearly? Identify two continuity relationships and possible reaction shots. Does the list establish final scene duration? Ask the director and cinematographer one useful question each.

#### E24. Clarify a delivery brief

The following limits are invented classroom requirements:

> Supply one picture review file at 1920 × 1080 pixels and 25 fps. It must have stereo reference sound and visible version identification at the beginning. Supply subtitles separately. Use the approved file-naming pattern. The deadline is Friday at five.

List at least six missing specifications or ambiguities that matter for delivery. Include the precise date and time zone, the meaning of “review,” subtitle format, file naming, and the required container/encoding information. Write a concise clarification email. Do not select a codec, subtitle format, or naming pattern and pretend it has been approved.

#### E25. Write a handover for your specialism

Choose one assignment and write 130–170 words from the supplied facts.

**Directing:** In scene 4, Ivo should delay answering because he recognises the envelope. Maja interprets the silence as reluctance. The film should leave that interpretation uncertain. Ask the editor to test the pause before Ivo speaks without explaining the character's history through added dialogue.

**Cinematography:** The intended image makes Maja easy to distinguish from the background while retaining visible detail in the foyer. In the review copy, the noticeboard behind her attracts more attention than intended. The original recordings have not yet been checked. Describe the intention and request an assessment without claiming that the recording is unusable.

**Editing:** Two versions of scene 4 are available. Version A cuts to Maja during Ivo's pause; version B stays on Ivo. No other shot lengths differ. Ask for a decision about whose uncertainty the audience should follow. Explain the choice through the supplied difference, not an invented audience test.

#### E26. Identify the current version

The shared folder contains:

```text
LastShowing_scene04_v02_review.mp4
LastShowing_scene04_v03_review.mp4
LastShowing_scene04_FINAL.mp4
LastShowing_scene04_v03_notes.txt
```

The producer's message states: “Use v03 for the review on 16 October. The file labelled FINAL is an old export and must not be used for that review.”

Identify the current review file and the authority for that choice. Explain why a filename alone does not establish approval. Propose a consistent name for the next review version and write a two-sentence update that identifies the new file, its purpose, and the earlier version it replaces for review. Do not delete the earlier files as part of this language exercise.

### Correspondence and international collaboration

#### E27. Write the subject and opening

For each situation, write an informative email subject and a two-sentence opening. Make the requested action clear.

1. You need the producer to confirm the deadline for the next review export.
2. An editor has sent useful notes; you are confirming which two revisions you will make.
3. You are contacting a festival for the first time because its submission instructions do not explain whether an English subtitle file is required at the initial stage.

Use a collegial tone for an established collaborator and an appropriate opening for a first contact. Avoid empty urgency: the situation does not establish an emergency.

#### E28. Request missing material

Write an email of 100–130 words from these facts:

> You are editing scene 4. Camera clips and a camera report are available. The folder has no separately recorded location sound files and no sound report. The producer has asked for a dialogue review on Tuesday 20 October at 14:00 Ljubljana time. You need to find out whether the missing material was recorded and where it is stored. You can organise the picture material while waiting. You cannot promise a dialogue review until the sound situation is clarified.

Name the missing items, ask for an owner or location, explain the effect on the task, and state what can proceed. Do not accuse anyone of losing files or promise restoration of material that may not exist.

#### E29. Decline one deadline and offer a workable alternative

The producer requests a full revised seven-minute cut by 12:00 tomorrow. You have already agreed another delivery that morning. You can supply the revised opening by 12:00. Alternatively, you can supply the full cut by 17:00 if the producer approves the scene order by 10:00.

Write 90–120 words. Acknowledge the request, state the constraint, offer the two options, and identify the dependency. Avoid excessive apology and vague promises such as “I will try my best.” Do not present the 17:00 option as unconditional.

#### E30. Remove date and time ambiguity

Rewrite this message so that a colleague in London cannot reasonably misunderstand it:

> Can you send it next Friday at five, our time? We'll look at it the next morning.

For this exercise, the agreed delivery is **Friday 16 October 2026, 17:00 in Ljubljana**. Use these supplied offsets: Ljubljana UTC+02:00; London UTC+01:00. The review is **Saturday 17 October, 10:00 in Ljubljana**. Name the deliverable as “scene 4 review, version 3.” Give both locations' times, or one explicit time zone and offset for each event. These offsets belong to the specified exercise dates; do not assume they apply throughout the year.

#### E31. Audit an AI-polished email

Original facts: the producer requested a review copy; its deadline remains unconfirmed; the editor has completed the picture assembly; sound work has not been reviewed; no screening approval has been given.

An automated rewrite says:

> Dear Producer, I am delighted to confirm that our final film is complete and approved for public screening. The sound has been professionally mastered, and I guarantee delivery by Friday. Please find the finished film attached.

Mark every unsupported claim or inappropriate commitment. Write a corrected 70–100-word email using only the original facts. Preserve a useful professional tone without adding praise, approvals, attachments, or completion claims that the evidence does not support.

### Stories, pitches, and professional explanation

#### E32. Write a logline

Use this original story outline:

> During the final week of a small cinema, trainee projectionist Maja discovers that the ending of a local amateur film is missing. She wants to reconstruct it before the farewell screening. Former projectionist Ivo remembers the film but will not explain why he left the cinema. Maja eventually chooses to show the surviving material and invite the audience to contribute their memories, allowing the farewell to acknowledge an incomplete history.

Write a logline of no more than 40 words. Make the protagonist, goal, and main obstacle clear. Then identify one detail you omitted and explain why. Do not invent a romance, crime, or historical revelation merely to make the premise sound more dramatic.

#### E33. Write a complete synopsis

Write a 150–180-word synopsis using the story in E32. You may add connective actions, but you must not change its ending or introduce a new central conflict. Use present tense consistently unless there is a clear reason to shift it.

Distinguish the synopsis from a promotional teaser: the reader needs to understand the outcome. Include Maja's change of approach. Afterwards, underline or list three verbs that carry the action more precisely than “is,” “has,” or “does.” State which added details are your own elaboration.

#### E34. Explain one choice to two audiences

The editor stays on Ivo during a five-second pause before his answer. A reaction shot of Maja exists but is not used in this version. The director wants the audience to examine Ivo's hesitation without knowing its cause.

Write two explanations of 60–80 words each: one for a professional editing memo, and one for a general audience reading a short production note. Preserve the same factual content. Use professional terminology where it helps the first audience, and explain the effect in accessible language for the second. Do not turn the director's intention into a claim about how every viewer will respond.

#### E35. Prepare a concise individual pitch

Prepare a one-minute pitch to the instructor using *The Last Showing* or your own existing project. Include the premise, intended audience experience, your professional contribution, and one concrete creative decision. Use a five-point outline with no more than ten words per point.

After speaking, answer: “What information would you need before committing to that plan?” Your answer should identify a real uncertainty. A pitch can be confident while acknowledging an unresolved production or creative decision. No new film, slide deck, or recording is required for this exercise.

### Feedback and post-production

#### E36. Turn a judgement into a usable note

Rewrite these comments as **observation → interpretation → proposed action**. Use the supplied evidence and distinguish personal response from fact.

1. “The opening is boring.” Evidence: four similar eight-second views precede the first character action.
2. “Her acting is wrong.” Evidence: Maja smiles before opening the envelope; the intended discovery comes after she reads it.
3. “The image is bad.” Evidence: in the review copy, the noticeboard attracts more attention than Maja's face.
4. “The dialogue is too academic.” Evidence: a hurried character says, “I would appreciate clarification of the circumstances surrounding your departure.”

Suggest a test or revision rather than announcing an unsupported diagnosis. Do not use a language exercise to prescribe hazardous production actions.

#### E37. Locate an editing note

Use **timeline timecode HH:MM:SS:FF, 25 frames per second, non-drop-frame**. The in-point is included; the out-point is excluded.

> File: `LastShowing_scene04_v03_review.mp4`  
> Range: 01:02:14:08–01:02:18:16  
> Observation: Ivo's mouth begins to move while Maja's preceding line is still audible.  
> Requested check: compare the picture and dialogue timing with the source recordings.

Write the note as a concise paragraph. Calculate the range's duration in frames and seconds. Does the note establish that the whole file has a sync problem? What further evidence would you need before requesting an offset for the entire soundtrack?

#### E38. Write a reproducible issue report

These are the available observations:

> The current review file is v03. In two playbacks in the same player, a single black frame appears between shots 4B and 4D. The source timeline uses 25 fps non-drop-frame timecode. The frame is at timeline timecode 01:03:05:12. The reviewer has not tested another player or checked the editing project. The previous review file has not been compared.

Write 100–130 words with a clear subject, the observed behaviour, steps already taken, limits of the evidence, and a specific request. Do not write “This happens on every computer” or attribute the problem to corruption without evidence. Explain why naming both the file version and timecode convention helps the recipient.

#### E39. Respond to an editorial request

The director writes:

> Please shorten scene 4 by about fifteen seconds, retain Ivo's initial pause, and keep the envelope label readable. I am more concerned about repeated information than about making every individual shot shorter.

The current cut repeats Maja's question in two places. Removing the second instance and its following reaction would shorten the scene by approximately eleven seconds. You have not tested additional reductions.

Write a 100–130-word response. State what you will test, what it preserves, and what remains to be evaluated. Ask a useful question if needed. Keep proposed changes distinct from completed work.

### Dialogue and subtitles

#### E40. Rewrite dialogue without flattening the character

Context: Maja is in a hurry and knows Ivo well. She wants him to explain why he left the cinema. Ivo avoids a direct answer.

> **Maja:** I would appreciate clarification of the circumstances surrounding your departure from this institution.  
> **Ivo:** The matter to which you refer is no longer relevant to the present situation.  
> **Maja:** Nevertheless, your cooperation would facilitate the successful completion of our task.

Write a more plausible spoken version of no more than 55 words. Preserve Maja's question, Ivo's avoidance, and her renewed request. Then write a different version in which Maja deliberately uses exaggerated formality to mock Ivo. Explain how context changes the effect of the same register.

#### E41. Condense within stated limits

These are **classroom limits for this exercise**: at most two lines per event; at most 32 characters per line; at most 16 characters per second. Count spaces and punctuation, but exclude the line break from the total. Keep the supplied times. Preserve the condition, the accusation, and the correction.

| Event | Start → end, in hours:minutes:seconds,milliseconds | Dialogue |
|---|---|---|
| A | 00:00:10,000 → 00:00:14,000 | If the projector isn't back by six o'clock this evening, we won't be able to show the film. |
| B | 00:00:14,200 → 00:00:16,700 | But you absolutely promised me that it would be ready for today. |
| C | 00:00:16,900 → 00:00:19,900 | I promised that I would make an attempt. That's not the same thing. |

Write the three events and report the duration, total character count, and reading rate for each. Briefly explain any information you omit. These millisecond timestamps are different from the frame-based timecode in E37.

#### E42. Break lines for meaning

Rebreak this text into at most two lines of at most 32 characters each, without changing its wording:

> I thought you had kept the last ticket for me.

Then explain why these alternatives are less helpful:

```text
I thought you had kept the
last ticket for me.
```

```text
I thought you had kept the last
ticket for me.
```

Consider linguistic grouping as well as length. This example is not a universal rule against breaking phrases at line boundaries.

#### E43. Represent relevant sound without inventing it

Prepare English captions for this supplied event description. No audio recording is needed.

> Maja stands beside a closed door. Ivo speaks from the adjoining room: “Give me a moment.” A doorbell rings once. Maja turns towards the entrance. There is no music. The scene does not establish who rang the bell or how Maja feels.

The classroom task requires an off-screen speaker to be identified when necessary for comprehension and a significant non-speech sound to be represented concisely. Write the dialogue caption and a separate sound caption. Explain why “[sinister visitor arrives]” would add unsupported interpretation. Do not invent a music label merely because captions sometimes include music information.

### Language in context

#### E44. Express requirements and uncertainty

Rewrite each note as one clear sentence, preserving its stated strength.

1. Required: every review filename includes its version number.
2. Possibility, unverified: the visible issue comes from the export rather than the source recording.
3. Conditional commitment: you can supply the revised cut by 17:00 if the scene order is approved by 10:00.
4. Advice, not a rule: compare both versions before deciding which pause works better.
5. Hypothetical change: retaining the longer opening would leave less time for the final scene.
6. Prohibition in this production's instructions: do not distribute the unapproved review copy publicly.

Use **must, might, can…if, should, would,** and **must not** appropriately. Explain the difference between “must not” and “do not have to.”

#### E45. Report progress accurately

Choose a suitable tense and voice for each statement. More than one grammatical form may work, but its meaning must fit the evidence.

1. The editor completed the assembly yesterday. Begin: “The assembly…”
2. The team began checking names this morning and is still doing so. Begin: “We…”
3. No one has approved the final scene order yet. Begin: “The final scene order…”
4. Sound work will begin after the producer approves that order. Begin: “Once…”
5. At 11:00 yesterday, the editor was exporting a review copy when the producer called. Begin: “When…”

After rewriting, explain which statements describe completion and which describe a process or dependency. Do not convert “being reviewed” into “approved.”

#### E46. Repair grammar and collocation

Correct the following without changing the intended meaning:

1. “The equipments have arrived.”
2. “She gave me an useful feedback.”
3. “Who is responsible of the camera report?”
4. “We discussed about the revised ending.”
5. “Please explain me the difference.”
6. “The editor asked more time.”
7. “We need to make a decision until Friday.” (Friday is the latest acceptable date.)
8. “I look forward to receive your notes.”
9. “This version is different than the approved one.” (Use a broadly suitable formal construction.)
10. “The producer suggested to keep the first take.”

For items 1 and 2, explain the countability problem. For item 7, distinguish a deadline from an activity continuing through a period.

#### E47. Say the numbers clearly

Read the following individually to the instructor. For independent preparation, write how you would say the information in full.

1. Review version 13, compared with version 30.
2. A 15-second pause, compared with a 50-second pause.
3. Delivery at 14:30 on 16 October 2026.
4. Image dimensions of 1920 × 1080 pixels.
5. A range from timeline timecode 01:02:14:08 to 01:02:18:16 at 25 fps, non-drop-frame.

Use stress and, where helpful, confirmation to distinguish potentially confused numbers. When asked to repeat an item, repeat its label as well as its value: “The frame rate is twenty-five frames per second.” Intelligibility is the goal; there is no requirement to imitate a particular national accent.

#### E48. Audit a polished project description

Compare the rewrite against the authoritative facts in E12 and E32:

> *The Last Showing* is an award-winning ten-minute documentary featuring a large professional cast. It has already been completed and will premiere internationally next month. Its young director restores a lost masterpiece and reveals exactly why the cinema closed. All viewers will find the ending uplifting. The final files are ready for delivery.

Identify unsupported or contradictory statements. Rewrite the description in 90–120 words using only the supplied information. Distinguish a character from the film's director, a fictional short from a documentary, an intention from a measured effect, and an unresolved requirement from a completed task. Explain why fluent English does not make an account trustworthy.

### Integrated individual work

#### E49. Assemble the written submission

Use your own existing project or the supplied *Last Showing* material. No new production is required. Prepare **three connected texts in one file**:

1. A project description or synopsis explaining the project and its intended effect.
2. A substantial professional text for your specialism: a directing brief, a cinematography brief, an editing memo, or a technical explanation that you can support accurately.
3. An email that requests, confirms, or resolves something concrete connected to that text.

A useful preparation target is **600–900 words altogether**. The instructor announces the assessed length and deadline before submission. Use headings, identify the audience of the professional text, and give the document a clear filename and version. If you discuss your existing work, distinguish completed work from plans. If you use sources, acknowledge them and explain rather than reproduce their wording.

Revise the file against five questions: Does each text fulfil its purpose? Are professional terms precise? Are the facts consistent across the texts? Is the register appropriate? Have you checked grammar, filenames, numbers, and source claims? Submit the work through the channel announced by the instructor. Public publication is not a condition of passing.

The prescribed assessment has two components: **written work 50% and oral presentation 50%**, assessed through coursework. Both require a passing result; a negative result in either component requires an examination. This exercise gives a practical format for preparing the written component.

#### E50. Explain and defend your work individually

Prepare an individual presentation connected to E49. For practice, aim for four minutes; the instructor confirms the assessed duration and schedule. Explain the project, your professional contribution, two reasoned choices, and one limitation or unresolved question. You may use a simple outline or a small number of relevant images. A new film, public upload, or elaborate slide deck is unnecessary.

Afterwards, answer questions from the instructor. Prepare for questions such as:

1. What exactly do you mean by this technical term?
2. Why is this choice appropriate for your intended audience?
3. Which alternative did you consider, and what would it change?
4. What information would you need before making the next decision?
5. Which statement in your written work is based on a source, and how did you check it?

Assessment concerns understandable, organised professional English; appropriate terminology; language control; and the ability to explain, clarify, and respond. Identify your contribution accurately. Artistic ambition, production budget, a native-sounding accent, and public popularity are not substitutes for the language task.

### Answers and model responses

The calculations below follow the stated assumptions. For explanation, writing and diagnosis, other answers can be valid if they preserve the facts, identify the mechanism and communicate clearly. Model texts illustrate useful wording; expand them where a prompt requires a longer submission.

**Computer**

#### H01. Answer

Accept accurate identification and function statements supported by the demonstrated machine. A suitable description is: “This is the CPU cooler. It is mounted above the processor package and transfers heat from it to the air.” The visible cooler is not the CPU die. A memory module is not an SSD; a graphics card is a board containing a GPU rather than the name of every component on that board. Connector roles must be checked rather than inferred solely from colour or shape.

#### H02. Answer

In the schematic, the CPU's memory controller connects to DRAM; the illustrated NVMe SSD uses a processor PCIe connection; the USB path passes through the I/O chipset and its upstream link. Devices behind that chipset can share the upstream bandwidth. Other M.2 sockets can connect through the chipset or share lanes. The drawing does not establish the routing, electrical width or generation of the demonstration computer's sockets.

#### H03. Answer

Power = 1.2 × 5 = **6 W**. The hypothetical receiver classifies 0.2 V as 0 and 0.8 V as 1; 0.5 V is outside the specified valid ranges. An input level is not a measurement of the whole circuit's current or switching activity. In the simplified αCV²f model, the contribution becomes 1.2² = 1.44 times as large: a **44% increase**, with the other model terms fixed.

#### H04. Answer

For input 0, the pMOS pull-up conducts and the nMOS pull-down is off; Y approaches VDD. For input 1, the nMOS conducts and the pMOS is off; Y approaches ground. Actual transitions have finite delay, capacitance and potentially simultaneous conduction, with leakage even in nominally off devices. For NAND with A = 1 and B = 0, the series nMOS path is broken by the B-controlled device, while the B-controlled pMOS supplies a pull-up path. The output is **1**.

#### H05. Answer

00101101 = 32 + 8 + 4 + 1 = **45 = 0x2D**. Pattern 11111110 means **254 unsigned** or **−2 signed** in eight-bit two's complement. The sixteen-bit word is stored **34 12** in little-endian order and **12 34** in big-endian order. ASCII does not include č. The precomposed Unicode character U+010D has UTF-8 bytes **C4 8D**; its representation requires an agreed character encoding.

#### H06. Answer

The result is **34 = 00100010**.

| Bit | A | B | Carry in | Sum | Carry out |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 0 | 1 | 0 | 1 |
| 3 | 0 | 1 | 1 | 0 | 1 |
| 4 | 1 | 0 | 1 | 0 | 1 |
| 5 | 0 | 0 | 1 | 1 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 0 |

Unsigned 255 + 1 has low eight bits 00000000 and a carry out. Signed 127 + 1 has pattern 10000000, interpreted as −128, and is a signed overflow. These are different conditions; the retained bit pattern must be interpreted under the stated arithmetic rules.

#### H07. Answer

Q becomes **1, 1, 0, 1**, after the corresponding propagation delays. In the ideal edge-triggered model, changes between capture edges do not change the retained output. D must be stable for the specified setup interval before the capture edge and hold interval after it. Violating those requirements can make the output unreliable or metastable.

#### H08. Answer

DRAM uses a charge state accessed through a transistor; its contents require power, sensing/restoration and periodic refresh. Common SRAM uses powered feedback through cross-coupled inverters, with access transistors; it needs power but not DRAM-style cell refresh. NAND retains charge affecting a transistor's threshold, and ordinary persistent HDD recording retains magnetic patterns. Both require energy to read and write, but not continuous power simply to retain their recorded state within their retention limits. The NAND counts are **2, 4, 8 and 16 states**. A byte is an eight-bit logical unit; a physical cell can encode a different number of bits.

#### H09. Answer

2¹² = **4,096 bytes = 4 KiB**. Main memory and the SSD have different functions and access properties. Storage used for paging does not acquire ordinary DRAM latency or bandwidth. A cache hit finds the needed information in the cache; a miss requires access beyond it. Bandwidth concerns rate, while latency concerns delay. A large capacity alone establishes neither.

#### H10. Answer

0x17 = 23 and 0x0B = 11. LDI sets A to 23; ADDI sets it to **34 = 0x22 = 00100010**; STA writes 0x22 to address **0x90**, decimal 144. PC progresses through 0x00, 0x02, 0x04 and 0x06, where HALT leaves it. Replacing 0B with 0A changes the sum to **33 = 0x21 = 00100001**, stored at the same address.

#### H11. Answer

1. “Does this M.2 drive and socket use SATA or PCIe/NVMe?”
2. “Which data rate do the host port, cable and device support, and what sustained payload rate do we need?”
3. “How many lanes are wired and negotiated in this slot, at which PCIe generation, and are they shared?”
4. “Does this hardware and software combination decode this codec, profile, bit depth and chroma format in hardware?”
5. “Is that socket an input or an output, and which supported capture interface will receive the camera signal?”

The questions seek missing specifications. None assumes the equipment is defective.

#### H12. Answer

72 GB = 72,000 MB. At 180 MB/s, transfer time is **400 s = 6 min 40 s**. One gigabit per second corresponds to **125 MB/s** before overhead. The theoretical payload-only minimum is **576 s = 9 min 36 s**. Protocol overhead, file metadata, small random operations, source and destination limits, shared bandwidth and verification can increase the elapsed time.

#### H13. Answer

The buffer contains **1280 × 720 × 4 = 3,686,400 bytes**. Reading fifty each second represents **184,320,000 bytes/s = 184.32 MB/s**.

A model explanation:

> The SSD holds the file's encoded bytes. The application reads the required portions into accessible buffers, and a demultiplexer separates the video stream from the other contents of the container. A decoder reconstructs image samples, possibly using reference pictures. Image processing then performs operations such as scaling, colour conversion and composition. The display path presents a frame buffer, and the monitor turns the received representation into light. In this exercise, each working buffer contains four eight-bit components for every pixel, so reading fifty buffers each second requires 184.32 MB/s. The encoded file can have a lower bit rate because its codec represents the image sequence more compactly. Several processing passes can also read and write more data than this one-pass calculation. The storage bit rate and internal working-memory traffic therefore measure different stages of the system.

#### H14. Answer

Plausible explanations include inter-picture dependencies requiring reconstruction from earlier reference pictures, a difference in hardware decoding support, repeated random storage reads, insufficient working cache, or costly effects during interactive seeking. Inspect stream properties and decoder use; compare an appropriate intraframe proxy; test source-only playback with effects bypassed; observe storage and processor activity during the symptom. Free space is a capacity observation, not proof of adequate random-read performance. Another smooth file does not establish that the difficult file has the same representation.

#### H15. Answer

A suitable revision is:

> I copied the camera-card folder to [destination]. I have not yet established whether the complete required directory structure and every file were preserved. Similar file sizes are not a completed integrity check, and opening the project on this computer does not demonstrate an independent backup. Please confirm the required copy destinations and verification procedure. I will report the source and destination checks and retain the original card until the agreed media-handling requirements have been met.

Use “copied” if no conversion occurred. A completed handover must replace the missing details with observed results.

#### H16. Answer

Evaluate the accuracy of the chosen mechanism, clear sequencing, correct quantities and terminology, and responses to questions. For the processor option, a complete explanation connects stored instruction bytes to opcode decoding, operand selection, arithmetic, register capture and the store to memory. For playback, it distinguishes encoded file data from decoded working buffers and from physical light and sound. A statement that a component “makes it better” requires a more specific function or measurable consequence.

**Sound**

#### A01. Explain the signal path

One possible connected answer:

“Sound pressure moves the microphone diaphragm. The transducer converts that motion into an analogue electrical signal. The preamplifier amplifies the small voltage. Anti-alias filtering restricts the bandwidth entering the sampling system. The ADC samples and quantises the signal to produce digital values. The computer processes and stores those values, with optional encoding into a compressed representation. During playback, software decodes the stored representation and the DAC and reconstruction filtering produce a continuous analogue signal. The power amplifier drives the loudspeaker, whose diaphragm produces sound pressure in the room.”

The microphone input and loudspeaker output are acoustic. The preamplifier and filtered converter input are analogue electrical stages. Stored PCM and encoded files are digital representations. Different hardware can integrate several stages in one device.

#### A02. Diagnose the stage

The fader reduces the level of already captured data. It does not reverse overload in the interface’s input stage. Prevention requires an appropriate input level and gain arrangement at the stage that would otherwise overload; the microphone and any intermediate transmitter also have their own limits.

A floating-point file can preserve numerical values beyond the nominal ±1.0 reference when the complete recording system supports this. It cannot restore an analogue signal that was distorted before those values were measured. Identify the recorder architecture and the overload location before diagnosing recoverability.

#### A03. Sample rate and aliasing

1. `1/48,000 s ≈ 20.833 microseconds`.
2. `48,000/2 = 24,000 Hz`.
3. `48 − 31 = 17 kHz`. The 31 kHz and 17 kHz cosines agree at the sample instants.
4. The same sampled component could have come from either input. Filtering after sampling has no label identifying which physical origin produced it.
5. Each stereo channel still has 48,000 samples per second. There are two values in every sample frame.

For real capture, filtering and passband requirements must account for a practical transition region.

#### A04. Read the bytes

| Value | Hexadecimal word |
| --- | --- |
| +513 | `0201` |
| −513 | `FDFF` |

The negative word follows from `65,536 − 513 = 65,023`.

Little-endian, left first: `01 02 FF FD`.

Big-endian, left first: `02 01 FD FF`.

Correct conversion preserves the sample values. A raw stream also needs its sample rate, channel count and order, sample representation, byte order and packing/interleaving specified. The four bytes alone do not provide all this information.

#### A05. A converter’s decisions

| Trial | Voltage | Decision |
| --- | ---: | --- |
| `1000` | 0.5000 V | Clear the trial bit |
| `0100` | 0.2500 V | Keep the trial bit |
| `0110` | 0.3750 V | Keep the trial bit |
| `0111` | 0.4375 V | Clear the trial bit |

Final code: `0110`, decimal 6, representing 0.375 V.

The stated lower-edge model selects the highest code voltage that does not exceed the input. Nearest-level rounding would choose code 7, because 0.4375 V is closer to 0.43 V. Both answers are meaningful only with the quantisation convention specified.

#### A06. Plan the recording capacity

- Bit rate: `48,000 × 24 × 6 = 6,912,000 bit/s`.
- Byte rate: `6,912,000/8 = 864,000 B/s`.
- Thirty minutes: `864,000 × 1,800 = 1,555,200,000 B = 1.5552 GB`.
- Doubling the duration doubles this payload to 3,110,400,000 B.
- Using 96 kHz for the original 30 minutes also doubles the payload to 3,110,400,000 B.

Headers, metadata, padding and file-system allocation can add storage. Backups, working copies, review exports and other production files need additional capacity. Compression would require a different estimate.

#### A07. Buffers and monitoring

A 128-frame buffer spans `128/48,000 ≈ 2.667 ms`. A 512-frame buffer spans `512/48,000 ≈ 10.667 ms`.

A larger buffer generally gives processing and scheduling more time to meet playback deadlines. It can also increase monitoring latency. It does not directly improve converter precision.

The 2.667 ms figure describes one buffer. Complete round-trip latency can include input and output buffering, conversion, routing, plug-ins and scheduling. It must be measured or established from the complete path.

#### A08. Dither, noise and precision

1. **Inaccurate.** Bit depth concerns amplitude representation; sample rate concerns sample instants.
2. **Inaccurate.** Noise and distortion can limit effective measurement performance below the numerical word length.
3. **Accurate, with suitable dither.** The process controls the statistics of quantisation error at the relevant reduction stage.
4. **Inaccurate.** An unchanged copy does not perform another quantisation.
5. **Inaccurate.** Appropriate dither allows sub-LSB signal information to affect the statistics of quantised output. An undithered particular signal may nevertheless collapse to zero.
6. **Inaccurate.** Physical input stages and microphones can overload regardless of the eventual file’s numerical range.

#### A09. Read an audio CD precisely

- Stereo sample frames: 44,100.
- PCM payload: `44,100 × 4 = 176,400 B`, or 1,411,200 bits.
- Audio blocks: `176,400/2,352 = 75`.
- Small channel frames: `176,400/24 = 7,350`.
- Physical channel bits: `7,350 × 588 = 4,321,800` per second.

The physical channel includes coding, error correction, control and synchronisation overhead. Pit/land transitions represent the modulated physical channel; they are not a one-pit-per-PCM-bit map. Interleaving changes where audio-related symbols occur.

#### A10. Encode and decode a lossless prediction

First value: 200. Residuals: `+3, +2, −1, 0, −3`.

Reconstruction: `200 → 203 → 205 → 204 → 204 → 201`.

Uncompressed toy payload: `6 × 16 = 96 bits`.

Predictive toy payload: `16 + 5 × 4 = 36 bits`.

The 36-bit representation is 37.5% of the original payload, before headers and padding. A real decoder also needs enough information to identify the representation and reconstruct it. Different source material may require larger residuals or another coding mode. File metadata and byte alignment further affect the final size. These qualifications prevent a fixed compression-ratio claim.

#### A11. Describe a file without guessing

One possible description:

“The file contains four channels of 48 kHz, 24-bit signed integer PCM. WAVE is the container, and it includes production metadata. The four labels identify a boom, two radio-microphone sources and a production mix. The isolated sources and the mix should remain distinguishable during import. The channel count does not establish a stereo or surround presentation.”

The extension alone would not establish encoding, bit depth, sample rate or channel assignments.

| Name | Classification |
| --- | --- |
| FLAC | Lossless audio codec and native stream format |
| AAC | Lossy audio-coding family |
| BWF | WAVE-based production format and metadata conventions |
| Opus | Lossy audio codec |
| MIDI | Musical event/control messages, with associated transports and file formats |
| USB | A connection and transport system, not an audio codec |

#### A12. Trace a lossy generation

The final PCM must match the **specified 16-bit PCM sequence supplied to the FLAC encoder**, assuming successful lossless decoding and no intervening processing. It is not guaranteed to match the original PCM master that preceded the MP3 encoding.

Decoding MP3 reconstructs its encoded approximation. Writing that approximation into a larger uncompressed file does not identify the information lost earlier. Proper upsampling can create a different sample sequence at a higher rate while preserving the represented signal; it does not retrieve the original pre-encoding data.

#### A13. Separate four meanings of level

Turning down the playback amplifier changes the acoustic output, leaving the stored samples and the file’s measured programme properties unchanged. No calibrated relation to dB SPL has been given. The two stated readings also do not establish compliance with every delivery specification; channel layout, measurement rules, duration, tolerances and destination requirements still matter.

The sample sum is `0.8 + 0.6 = 1.4`. After a gain of 0.5, it is 0.7. Floating point can retain the intermediate 1.4. If an earlier stage clips it near the integer full-scale limit of 1, halving that clipped result gives a value near 0.5 instead. The missing amount cannot be inferred simply by lowering the fader.

#### A14. Find the timing problem

1. `0.180/3,600 × 1,000,000 = 50 ppm`, approximately.
2. `0.180 × 25 = 4.5 frames`.
3. The starting labels can agree while the clocks subsequently run at different rates.
4. Timecode identifies positions; word clock provides audio sample timing. A specific device may derive several clocks from one reference, but that must be established from its design and settings.
5. `44,100/48,000 = 0.91875 s`.

The offset magnitude does not identify which device ran fast or slow. Proper sample-rate conversion is different from playing unchanged samples under the wrong rate label.

#### A15. Write the technical handover

One possible answer:

The recording contains four isolated microphone tracks and a separate production mix. All files use 48 kHz, 24-bit integer PCM with BWF metadata. The project frame rate is exactly 25 fps. Please retain the track labels when importing the files so that the isolated sources remain identifiable.

The clap is aligned at the start of the first take. I have not yet checked the end, so this confirms an initial reference point rather than continuous synchronisation throughout the recording. Please compare the end of the take with the picture and report any changing offset. At these settings, one video-frame duration corresponds to 1,920 audio sample frames.

The original recordings are preserved. We will make the AAC review copy from the agreed master after the checks and any approved processing. That copy is intended for convenient review; the original PCM recordings remain available for editing.

One take contains a distorted shout. Its cause has not yet been established. Please identify the affected track and time range, then compare the isolated sources with the production mix. We should investigate whether the distortion arose in the microphone, input electronics or later processing before deciding what repair is possible. Lowering its playback level alone does not establish that the original waveform has been recovered.

Other answers can be equally strong if they preserve the facts, name the technical stages correctly and separate observations from hypotheses.

**Video**

#### V01

A defensible functional chain is tape playback → timing and level conditioning → decoding and sampling → digital capture → file storage and verification. The actual hardware may combine operations or digitise composite video before digital colour separation. The deck recovers the recording; time-base correction stabilises timing; colour decoding separates the required components; ADC represents measured amplitudes as numerical samples; the capture system writes media and metadata. An enlarged file cannot recreate lost fine detail, remove all recording noise, recover clipped information or reconstruct everything damaged by an earlier generation of copying. Any two correctly explained limitations are sufficient.

#### V02

The sequence from the sync edge is sync → back porch with burst → active video → front porch → next sync. The line rate is 625 × 25 = **15,625 lines/s**. Duration is 1/15,625 s = **64 µs**. The digital active line lasts 720/13,500,000 s = **53⅓ µs**. The whole line includes non-active intervals. At the same sampling rate, 864 samples represent its 64 µs duration. The digital active window is standardised and should not be casually equated with every analogue source’s exact visible interval.

#### V03

The woven picture places the moving edge at 100 on one set of alternating lines and at 110 on the other, producing a comb-like boundary. The field interval is **20 ms**; the pair rate is **25 pairs/s**. Discarding a field loses its recorded lines and, here, half the temporal observations. Field-rate deinterlacing can produce **50 progressive outputs/s**, estimating each field’s missing line positions. It cannot recover those unrecorded samples with guaranteed accuracy. PsF segments belong to one progressive acquisition picture, so they do not inherently contain the same between-field motion difference.

#### V04

64 = **01000000**; 128 = **10000000**; 255 = **11111111**. The RGB pixel requires **24 bits** before padding or additional channels. Ten bits provide **1024 codes**, maximum **1023**; twelve bits provide **4096 codes**, maximum **4095**. The primaries, transfer function and range are still required to interpret the components. Their ordering in a byte stream must also be specified. Numerical precision and physical colour are separate questions.

#### V05

Y′ = **0.0722**. Cb = (1 − 0.0722)/1.8556 = **0.5**. Cr = (0 − 0.0722)/1.5748 ≈ **−0.04585**. Rounding gives **Ycode 32, Cbcode 240, Crcode 118**. A negative colour difference represents a component below the weighted luma reference before unsigned offsetting; it is valid. A matrix tag tells a decoder how to interpret values. Replacing it without performing a required numerical conversion can misdescribe the same stored samples and change the displayed colour.

#### V06

| Sampling | Y′ | Cb | Cr | Total samples | Nominal bits |
| --- | --- | --- | --- | --- | --- |
| 4:4:4 | 24 | 24 | 24 | 72 | 720 |
| 4:2:2 | 24 | 12 | 12 | 48 | 480 |
| 4:2:0 | 24 | 6 | 6 | 36 | 360 |

Upsampling provides a denser output grid by reconstructing estimated chroma values. It does not uniquely recover the discarded original colour detail. The reconstruction must respect the source and destination chroma sample positions. These counts assume the stated progressive, even-sized image and omit memory padding.

#### V07

The nominal rate is:

`1920 × 1080 × 50 × 2 × 10 = 2,073,600,000 bit/s`

This is **259.2 MB/s**. Ten minutes requires **155.52 GB** of picture payload.

The viewing version requires:

`16,000,000 × 600 ÷ 8 = 1,200,000,000 bytes = 1.2 GB`

Possible differences include audio payload, container metadata, padding or alignment, and deviation of a target average bit rate from the measured average. For an interface rate, blanking and transport overhead are further distinctions. The smaller file may still require a more demanding decoder.

#### V08

The residual is **1, 3, 8, 9**. The separate coefficients divided by 8 and rounded become **2, 1, −1**. Reconstruction gives **16, 8, −8**, which differs from **19, 5, −7**. Quantisation is the explicitly irreversible step in this example. Entropy coding preserves the quantised symbols; exact recovery of 2, 1 and −1 does not contain enough information to identify which original values rounded to them. An invertible transform without discarded precision would not itself require information loss.

#### V09

One valid decoding order is **I0, P3, B1, B2**. I0 is available first; P3 can then be reconstructed from it; B1 and B2 can use both references before being displayed in their proper positions. B1 and B2 depend on P3 in this example. Some contemporary coding structures allow B pictures to serve as references, so the example’s restriction is not universal. An I picture has intra-coded image content, but subsequent dependencies and decoder state can extend across a nominal GOP boundary. A specified refresh or random-access structure is needed.

#### V10

The extension identifies packaging, and the dimensions identify the picture grid. Neither establishes decoder workload. Check at least five relevant properties: codec, profile, level, precision, chroma sampling, frame rate, GOP structure, actual bit rate, supported hardware decoding and software configuration. B has twice the picture rate and a different sample representation and codec. That does not by itself quantify total workload, but it invalidates an assumption of equivalence.

Rewrapping may help a compatible stream enter a better-supported container workflow; it does not change its fundamental picture coding. A transcode can replace difficult coding with an editing-friendly representation. A proxy can provide a lighter linked working copy while retaining originals for finishing. Preserve and verify the frame correspondence.

#### V11

1. Investigate a range mismatch. Compare the player’s expected input range with the file’s documented sample scaling and inspect known black values.
2. Investigate the missing or incorrect input/output colour transform. Identify the camera log curve and colour space, then use the matching display conversion.
3. Investigate incorrect metadata substitution. Restore the correct source interpretation and perform an appropriate HDR-to-SDR rendering conversion.
4. Investigate damage already present upstream. A higher-precision output does not restore values absent from the eight-bit source.

UHD specifies picture dimensions, wide colour gamut concerns the colour range, and HDR concerns the light range and its representation/display. More than one may apply to the same programme.

#### V12

At 25 fps, the interval is (18 − 14) × 25 + (16 − 8) = **108 frames**, or **4.32 seconds**. The next labels are **00:01:00;02** and **00:10:00;00** respectively. Labels are skipped in the first case; no recorded pictures are removed.

One possible handover note:

> The preservation master retains the captured field structure and the documented colour interpretation. I propose a ten-bit 4:2:2 lossless file, with the final container agreed with the archive. The accompanying record identifies the cassette, playback deck, capture settings, field order, audio channels and any observed defects. I have checked the picture and sound throughout the transfer and retained a checksum for subsequent integrity checks. If editing requires a different representation, I will create a clearly identified working copy and verify its correspondence with the master. The viewing copy will be deinterlaced for progressive playback and encoded at a suitable delivery rate. It will remain a derivative; the master and its documentation will be retained separately.

Other well-reasoned format proposals are acceptable. A checksum can support later integrity checking; it cannot by itself establish that a capture was complete or technically correct.

**Cameras**

These are model answers and marking guidance. Alternative wording is valid when the technical meaning, assumptions and units are correct.

#### C01. Answer

Example: “This is the lens mount. It is the mechanical interface at the front of the camera body. It secures the lens and establishes its position relative to the sensor. Its flange focal distance is different from the lens's focal length.”

Other answers should identify the actual equipment. Do not award credit merely for naming a BNC-shaped connection without checking its labelled function. A camera may set aperture electronically rather than through a dedicated ring.

#### C02. Answer

v = fu/(u − f) = 75 × 600/525 = **85.714 mm**. Magnification m = −v/u = **−1/7**. Image height is **−17.143 mm**. The image is inverted in the thin-lens model.

A ray parallel to the optical axis emerges through the image-side focal point; a ray through the lens centre continues straight in the approximation. Their intersection fixes the image tip. Real compound-lens principal planes and the mechanical mount reference are different; the calculation is not a camera mounting specification.

#### C03. Answer

Using 2 arctan(w/2f), mode A gives approximately **54.4°**, and mode B approximately **37.8°**. Both use the same 35 mm focal length. A fixed-camera crop retains the same perspective within the recorded region. Moving the camera changes viewpoint and can change near/far size relationships, occlusions and background relationships. A complete explanation identifies both the crop and the physical move.

#### C04. Answer

Opening f/5.6 → f/4 → f/2.8 adds **two stops**. Shortening 1/50 s to 1/100 s removes **one stop**. The net change is **one stop more exposure**. Add one stop of ND: **ND 0.9** replaces ND 0.6, using conventional rounded labels.

The wider aperture can reduce depth of field under the stated comparison; the shorter exposure reduces motion blur. Matching total exposure does not cancel those geometric and temporal changes. Flicker behaviour may also change.

#### C05. Answer

T = 2/√0.64 = 2/0.8 = **2.5**. Ideal lens B matches at **f/2.5**. The lenses' entrance-pupil geometry, optical design and rendering need not match; equal T-number alone does not establish equal depth of field.

ND8 commonly denotes an eightfold filter factor: **1/8 transmission, three stops**. Optical density 8 would instead mean transmission 10^−8. Verify the manufacturer's notation.

#### C06. Answer

1. Photons can generate charge carriers; the sensor integrates charge, readout circuitry produces an analogue signal, and an ADC assigns numerical codes.
2. CCD and CMOS name sensor/readout technologies. Either can form part of a digital camera when the measured signal is digitized.
3. A Bayer site supplies one filtered measurement. Demosaicing estimates missing colour components at output locations.
4. CMOS sensors can implement rolling or global exposure modes; consult the design and camera mode.
5. The aperture is an opening. The iris changes it, while the indicated f-number describes a ratio involving focal length and entrance-pupil diameter.

#### C07. Answer

Mean detected signal: **3,000 electrons**. Expected voltage: **0.300 V**. Digital code: **300**. Ten-bit binary: **0100101100** = 256 + 32 + 8 + 4.

Photon-limited standard deviation is √3,000 ≈ **54.8 electrons**. At 100 μV/electron this is approximately **5.48 mV**, or **5.48 ADC codes**. Finer quantization describes the fluctuating measurement more precisely but does not remove the physical fluctuation.

#### C08. Answer

End times: **8, 13, 18 and 23 ms**. Frame rate: **25 fps**. Each row exposes for **8 ms**. First-to-last start skew: **15 ms**.

The moving feature is measured at different positions at different row times. With all rows exposed from 0 to 8 ms, that timing skew disappears, but motion blur can remain within the common 8 ms interval. A global-shutter sensor can store the simultaneous measurements and read them out afterwards. The supplied timing does not establish every detail of that later data transfer.

#### C09. Answer

There are **200 captured frames**, presented for **8 seconds** at 25 fps. The 180° exposure is 180/(360 × 100) = **1/200 s = 5 ms**. A 25 fps, 180° capture exposes for 20 ms, so a subject moving at the same image velocity travels four times farther during each exposure.

The picture has been slowed to one quarter of real-time speed. The sound needs an intentional treatment or different use; an unchanged two-second soundtrack cannot track the whole eight-second visual action. Whether pitch is preserved during stretching is a separate processing decision.

#### C10. Answer

A good correction explains that raw formats retain sensor-related data but can include calibration, nonlinear encoding, compression or partial demosaicing. Log describes transfer encoding, while a codec defines coding/compression. ISO/EI controls can change analogue gain, digital scaling, monitoring or metadata depending on the mode; additional photons require an actual change to illumination or optical exposure.

A LUT's effect depends on its position in the signal path and whether that output is recorded. White-balance flexibility depends on the recorded representation and channel information; clipped capture data cannot always be reconstructed. An answer should request the camera model, recording mode, raw/codec specification and output routing before claiming how this particular recording was made.

#### C11. Answer

1. Possible aliasing or moiré: compare framing, focus and a different sampling mode; display scaling can also create patterns.
2. Possible light modulation: hold camera settings constant while testing the lamp's dimmer level, then test exposure timing; several light sources or display refresh can complicate the result.
3. Possible interpretation mismatch: compare the recording's declared transfer function, input transform and monitoring LUT routing; actual underexposure or a misconfigured display is another possibility.
4. Possible focus error: inspect at appropriate magnification and check the intended focus plane; movement, lens problems or processing can also affect sharpness.
5. Possible write-performance or compatibility problem: inspect the error and compare supported media at the required mode; heat, power or another recording limit may be responsible.

Credit plans that isolate variables and describe evidence clearly.

#### C12. Answer

Video: 100,000,000 × 60/8 = **750,000,000 bytes**. Audio: 48,000 × 24 × 60/8 = **8,640,000 bytes**. Total: **758,640,000 bytes = 758.64 MB**. Captured frames: **1,500**. Actual files include overhead and may vary if the stated constant-rate assumption does not apply.

The report should distinguish specified conditions from proposed choices and state whether the LUT affects monitoring, recording or both. The signal-path explanation should include optics, exposure, sensor charge, analogue readout, conversion, appropriate image interpretation/processing, codec/file writing, verified copying and software decoding. It must not imply that a Bayer photosite measures full RGB or that the copied file is a second optical capture.

Examples of responsibilities: choosing photographic contrast and aperture; maintaining focus and operating the camera; organizing and verifying recorded media. The production should agree who performs and confirms each task rather than assuming every small crew has a dedicated person for every job.

**Professional English and integrated work**

Alternatives may preserve the facts and fulfil the task equally well. Short model passages illustrate wording; develop them when the exercise requires a longer text.

#### E01–E03. Introductions and clarification

**E01.** “I am a second-year cinematography student. I have operated the camera on two short student films, and I am interested in how framing directs attention.” Distinguish this experience from leading a professional department and name a learning aim.

**E02.** “I operated the camera on two short exercises, one with a fixed camera and one with camera movement. Another student planned the lighting. I want to explain framing and movement more clearly in English.” “Professional” and “very good” are unsupported.

**E03.** “Which version do you need, by when, and for whom? If you mean the approved review version, I can prepare it once you confirm the details.” Clarify whether “tighter” concerns duration, pacing, or framing; clarify what “clean” removes or retains.

#### E04–E11. Terminology

**E04.** (a) Director; (b) second assistant camera; (c) cinematographer; (d) location manager; (e) first assistant camera; (f) production sound mixer; (g) producer; (h) gaffer; (i) editor, working with the relevant creative decision-makers; (j) sound editor. These answers follow the supplied division of responsibilities, not a claim about every crew.

**E05.** Connect information to a decision. An editor may need to know the intended performance or why a view is missing. Naming the dramatic aim helps more than “Choose the best take.” Other specialisms should be equally concrete and distinguish proposals from approval.

**E06.** 1 take; 2 shot; 3 set-up; 4 scene; 5 sequence. For 6: “Please record another take using the same camera arrangement, dialogue, and blocking.” “Shot” has several professional uses, so the added context resolves the ambiguity.

**E07.** 1 blocking; 2 framing; 3 coverage; 4 continuity; 5 eyeline match; 6 montage. Item 6 specifies compression of time as its function. A list of short shots alone would not establish the same narrative purpose.

**E08.** “Maja should appear nearer the image's left edge”; “Place the noticeboard beyond Ivo, farther from the camera”; “Maja looks towards the empty seat beside the doorway”; “Use the angle looking from doorway to counter.” Ask whose viewpoint defines “left” when unclear.

**E09.** 1 “Frame Maja's face in close-up”; shot size does not specify a lens. 2 “Maja's face is out of focus; exposure appears acceptable.” 3 “The image has a large depth of field.” 4 “Move the camera closer to the actor.” 5 “Should Maja remain the same size while more surroundings become visible?” Clarify before selecting a method.

**E10.** Assembly joins scenes; a rough cut develops structure and selection; a fine cut refines timing and cut points. These labels vary by workflow. Picture lock is an agreed status. Conforming matches finishing material to the edit; grading addresses colour and tone; mixing combines sound. Later picture changes can require coordinated revisions. An approved cut may still need finishing and delivery checks.

**E11.** 1 “I directed a documentary last year.” 2 “This is the current working version.” 3 “Please check the spelling of the names in the credits.” 4 “We need a sensitive microphone.” 5 “Editing begins on Monday.” 6 “Please save the file in the shared folder.” Choose by meaning and collocation. In item 4, *sensitive* is the intended adjective; suitability for recording a quiet sound also depends on noise and the recording setup. See [Shure's explanation of microphone characteristics](https://www.shure.com/en-US/docs/education/house-of-worship-audio-systems).

#### E12–E17. Comprehension and sources

**E12.** Confirmed: seven-minute fiction, two speaking characters, six extras, two settings, recorded test, audible ventilation, one agreed access day. Unresolved: delivery date and specifications, sound treatment, need and permission for another visit. “Restrained rather than nostalgic” expresses intention, not a measured response.

**E13.** Observations: three static shots, no dialogue, eight seconds each. Interpretation: the building has outlived its audience. Evaluation: “For me…”. Action: test removal. Formal wording: “The fourth similar shot may weaken the progression; a version without it would allow comparison.”

**E14.** A: delivery; B: camera options; D: role; E: initial submission. E does not fully specify screening delivery. A reliable manual for another model may be irrelevant; an unexplained search summary cannot justify a consequential specification.

**E15.** A and B concern different purposes. C mistakes a review copy's dimensions for a final requirement. Model correction: “The 1280 × 720 file is for review of content and timing. The producer has specified 1920 × 1080 for the final picture file, with the remaining details to follow in the approved delivery brief. Could you send us that brief when it is confirmed? We should keep the review and final requirements distinct.”

**E16.** Start 09:15; arrival 08:45; Ivo cannot arrive before 10:00; projection room after lunch unconfirmed; shot list v03 current, v02 retained; questions to producer before 16:00 that afternoon. “We will start with Maja's entrance at 09:15 after arriving at 08:45. I will bring version 3. The conversation follows Ivo's arrival; the projection room is still awaiting confirmation.”

**E17.** Collocations: “record additional coverage,” “check continuity,” “record room tone,” “agree picture lock.” Example: “The editor requested additional coverage of Maja's reaction.” Include context, an honest source label, and any translation uncertainty.

#### E18–E21. Operational communication

**E18.** Examples: “Could you email shot list v03 to the director before 16:00 and confirm that it has been sent?” “Could the sound department assess the ventilation audible beneath the dialogue in take 2 and report whether the recording is usable?” “Please repeat take 3's dialogue and blocking using the revised framing in the approved shot list, and record the new take's identifier in the camera report.” “Please send the revised scene order to the editor and confirm which version it replaces.”

**E19.** Name the review copy, join, reproducible symptom, and unconfirmed timecode. Request comparison with project and source. The camera is only one possible point in the workflow; none of the source recordings has been checked.

**E20.** Start with Maja alone, then schedule shared material after Ivo arrives. Respect the noon limit and ask about the projection room. Completion within the available time is not established.

**E21.** Read “version three”; “fifteenth of October, twenty twenty-six”; “eight forty-five”; “nine fifteen”; “nineteen twenty by ten eighty pixels”; “twenty-five frames per second”; and “one hour, two minutes, fourteen seconds, eight frames.” Other clear number readings are acceptable. Do not call the final timecode component milliseconds.

#### E22–E26. Documents

**E22.** Ivo's 08:30 call and the conversation's 09:15 start conflict with his 10:00 availability. The order and possibly both scene slots need confirmation. Request a revised call sheet from the person responsible for the schedule. An editor's silent redistribution could create competing instructions without approval.

**E23.** The insert shows label detail. Envelope position, opening action, Maja's look, and Ivo's response need coherent relationships. 4B/4D can provide reactions. The list specifies coverage, not final duration. Ask about intended emphasis or the relationship between views.

**E24.** Missing points include calendar date, time zone, purpose and approval status, container/encoding requirements, subtitle format and language, naming pattern, transfer location, and precise version-identification treatment. Ask for the approved brief. “I will send an MP4 and an SRT” is an assumption until those formats are agreed.

**E25.** Directing: preserve uncertainty and test the pause. Cinematography: distinguish intention from the review image and request source assessment. Editing: explain the difference between Ivo's close-up and Maja's reaction without claiming proven audience effects. Identify the decision the handover enables.

**E26.** Use `LastShowing_scene04_v03_review.mp4`, because the producer specifies it for that review. `FINAL` does not override the message. A possible next name is `LastShowing_scene04_v04_review.mp4`. The update must say what changed and which file to use; the new number alone does not mean approval.

#### E27–E31. Correspondence

**E27.** Possible subjects: “Scene 4 review — deadline confirmation”; “Scene 4 notes — two revisions confirmed”; “English subtitles for initial submission — clarification.” Open by stating the relevant context and request. The festival message should distinguish initial submission from later screening delivery.

**E28.** “Could you confirm whether separate location sound was recorded for scene 4 and where we can access the files and sound report? I have the camera clips and camera report and can organise the picture material meanwhile. The dialogue review is requested for Tuesday 20 October at 14:00 Ljubljana time; I need the sound information before confirming that delivery.” Expand politely without inventing blame or missing technical facts.

**E29.** “I cannot complete the full revised cut by noon alongside the delivery already agreed for that morning. I can send the revised opening at 12:00, or the full cut at 17:00 if you approve the scene order by 10:00. Which option would be more useful?” The condition belongs with the second offer.

**E30.** Delivery: Friday 16 October 2026, 17:00 Ljubljana / 16:00 London. Review: Saturday 17 October, 10:00 Ljubljana / 09:00 London. Include “scene 4 review, version 3.” Avoid “next Friday,” which depends on when the recipient reads the message.

**E31.** Unsupported claims: final film complete; public-screening approval; professionally mastered sound; guaranteed Friday deadline; attachment and finished-file status. A correction confirms the picture assembly only, states that sound has not been reviewed, and asks for the review deadline and delivery details. It must not imply that the sender attached a file when no attachment is supplied.

#### E32–E35. Story and pitch

**E32.** “Before her cinema's farewell screening, a trainee projectionist tries to reconstruct a missing film ending with help from a former projectionist who refuses to discuss his past.” This 27-word logline preserves goal and obstacle. The outcome belongs in the full synopsis.

**E33.** Include the final week, Maja's discovery and goal, Ivo's incomplete cooperation, and the decision to show surviving material and invite memories. Keep tense consistent and identify added connective actions. An invented solved mystery changes the premise.

**E34.** Professional version: “The cut holds on Ivo for the five-second pause rather than using Maja's available reaction. This choice directs attention towards his hesitation while withholding its cause.” General version: “We stay with Ivo while he searches for an answer. The viewer has time to watch him, but the scene does not explain what he is hiding or whether he is hiding anything.” Neither guarantees a uniform response.

**E35.** Outline: protagonist/problem; screening deadline; Ivo's uncertainty; departmental contribution; choice requiring information. The follow-up answer names a genuine dependency, such as location access or available performances.

#### E36–E39. Feedback and reports

**E36.** “Four similar eight-second views precede any action. I find the fourth adds little information. Could we test removing it?” Other notes identify the smile's timing, competing noticeboard, or unsuitable register and propose a focused test.

**E37.** Duration: 108 frames, or **4.32 seconds**. The out-point is exclusive. The overlap could be intentional; the observation does not establish a global sync problem. Check source sync, other positions, and the export before recommending an offset.

**E38.** Identify v03, the single black frame, timeline timecode 01:03:05:12, and the two repeat playbacks in one player. State that other players, the project, sources, and v02 have not been checked. Request comparison at that position. Reproducibility within one test environment is narrower than evidence that all computers behave identically.

**E39.** Propose removing the repeated question and following reaction, estimating about eleven seconds. Confirm that the initial pause and label readability remain priorities. State that further reductions need testing and ask whether an approximately eleven-second reduction would be acceptable if it preserves the scene better. Do not announce a completed fifteen-second reduction.

#### E40–E43. Dialogue and captions

**E40.** “Why did you leave?” / “That was a long time ago.” / “I know. Will you help me or not?” The mocking version deliberately retains excessive formality. Plausibility depends on character, relationship, and purpose.

**E41.** One possible set is shown below. The counts exclude line breaks and include spaces and punctuation. These are model condensations; compare their emphasis with the longer dialogue.

```text
A
No projector by six,
no film tonight.

B
You promised
it would be ready today.

C
I promised to try.
That's different.
```

| Event | Duration | Characters | Characters per second |
|---|---:|---:|---:|
| A | 4.0 seconds | 36 | 9.0 |
| B | 2.5 seconds | 36 | 14.4 |
| C | 3.0 seconds | 35 | 11.67 |

All lines fit. A preserves condition and consequence; B preserves accusation; C distinguishes trying from guaranteeing success. Redundant emphasis is reduced. Alternatives may retain more wording within the limits.

**E42.** A useful break is:

```text
I thought you had kept
the last ticket for me.
```

It preserves “the last ticket” as a phrase. The first supplied alternative separates the determiner from the following phrase; the second separates “last” from “ticket.” Both supplied versions fit the line limit, so the decision concerns linguistic grouping as well as length.

**E43.** “[Ivo] Give me a moment.” Then “[doorbell rings]”. The description establishes neither the visitor's identity nor the bell's emotional significance. The speaker label clarifies the off-screen voice; no music is supplied.

#### E44–E48. Language and verification

**E44.** 1 “Each review filename must include its version number.” 2 “The issue might come from the export rather than the source.” 3 “I can send the revised cut by 17:00 if the order is approved by 10:00.” 4 “You should compare both versions.” 5 “A longer opening would leave less time for the final scene.” 6 “You must not distribute the unapproved review copy publicly.” “Must not” prohibits; “do not have to” removes an obligation.

**E45.** 1 “The assembly was completed yesterday.” 2 “We have been checking the names since this morning.” 3 “The final scene order has not been approved yet.” 4 “Once the producer approves the scene order, sound work will begin.” 5 “When the producer called at 11:00 yesterday, the editor was exporting a review copy.” Only item 1 describes confirmed completion of the stated task.

**E46.** 1 “The equipment has arrived.” 2 “She gave me useful feedback.” 3 “responsible for”; 4 “discussed the revised ending”; 5 “explain the difference to me”; 6 “asked for more time”; 7 “by Friday”; 8 “look forward to receiving”; 9 “different from”; 10 “suggested keeping the first take” or “suggested that we keep the first take.” “Equipment” and “feedback” are uncountable in these uses. “By” sets the latest point; “until” describes continuation up to a point.

**E47.** Distinguish “thirteen/thirty” and “fifteen/fifty” through stress, articulation, and confirming labels. Standard date/time readings can differ while preserving the values. The final timecode component counts frames. Precision matters more than accent.

**E48.** The rewrite invents awards, changes seven minutes to ten and fiction to documentary, inflates the cast, announces completion and a premiere, confuses Maja with the director, invents restoration and an explanation of the closure, predicts every viewer's response, and asserts ready delivery files. A corrected description should retain the actual story, modest production facts, and unconfirmed delivery requirements.

#### E49–E50. Integrated work

**E49.** Three texts need distinct purposes and consistent facts. Directing connects choices to dramatic relationships; cinematography connects images to intentions and constraints; editing identifies material, decisions, and consequences. The email requests or confirms something arising from that work. A text must not present a production decision as approved when the memo identifies it as unresolved.

**E50.** Explain choices in a clear progression, use terms accurately, answer the question asked, and qualify uncertainty. “I cannot confirm that from the available material; I would check…” can be a precise professional response. Follow-up answers supply individual language evidence.
