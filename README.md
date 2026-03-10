# rhinoBot
![Skyscraper Cluster](./image.png)

A collection of professional Rhino skills designed to enable Gemini CLI to perform sophisticated parametric modeling in Rhinoceros via the Rhino MCP Server.

## 🏗️ Available Skills

### 1. rhino-skyscraper-generator
A parametric tool for creating structurally realistic skyscrapers with central cores, floor slabs, and complete column grids.

#### **Key Features:**
- **Parametric Height**: Generate buildings from 10m up to 300m+.
- **Structural Integrity**: Includes a central core and a distributed column grid (e.g., every 8 meters).
- **Floor Tapering**: Automatic footprint setbacks for architectural variety.
- **Layer Organization**: Automatically sorts objects into `Core`, `Slabs`, and `Columns` layers.

### 2. rhino-artsy-vase-generator
A tool for generating contemporary, sculptural, and fully hollow 3D vases in Rhino, leveraging advanced double-lofting and Boolean difference techniques.

#### **Key Features:**
- **Biomorphic & Organic Shapes**: Create asymmetrical "pinched," "totemic," or "elongated" vase designs.
- **Fully Hollow / Functional**: Models are properly hollowed out with adjustable solid wall thickness (capable of holding water in reality).
- **Customizable Profiles**: Easily modify the shifted circular profiles to create endless variations.

---

## 🚀 Installation

To add these skills to your Gemini CLI, ensure you have the [Rhino MCP Server](https://github.com/jingcheng-chen/rhinomcp) running, then execute the install command specifying the path to the desired skill.

For the **Skyscraper Generator**:
```bash
gemini skills install https://github.com/LeoYuanjieLi/rhinoBot --path rhino-skyscraper-generator --consent
```

For the **Artsy Vase Generator**:
```bash
gemini skills install https://github.com/LeoYuanjieLi/rhinoBot --path rhino-artsy-vase-generator --consent
```

After installation, enable the skill(s) in your active session:
```bash
/skills reload
```

---

## 🛠️ How to Use

Once installed, you can simply ask Gemini to generate geometry for you:

> "Build a 200m skyscraper at the origin with a column grid every 10 meters."
>
> "Create a cluster of 5 buildings with varying heights and shapes."
>
> "Generate a contemporary, artsy vase with an elongated neck."

Gemini will automatically leverage the bundled Python scripts to perform the modeling work in your active Rhino document.

---

## 📈 Performance
In testing, generating a complex, structurally complete skyscraper using this skill is **~100x faster** than manually researching and coding the same geometry from scratch.
