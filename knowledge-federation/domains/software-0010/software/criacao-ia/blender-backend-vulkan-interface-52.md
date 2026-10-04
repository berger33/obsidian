---
id: software.criacao_ia.tranche04.000368
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.blender.org/manual/en/latest/editors/preferences/system.html", "https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender 5.2: o backend da interface é escolha (OpenGL × Vulkan) com custo de reinicialização

## Em uma frase
As preferências de System expõem 'Backend' para os gráficos de display (OpenGL tradicional, Vulkan moderno) e 'Device Vulkan' para escolher a GPU da UI em máquinas multi-GPU; trocar qualquer um exige reiniciar o Blender.

## Por que importa
É a primeira vez que a UI do viewport entra em política de GPU explicitamente: notebooks com iGPU+dGPU renderizam a interface e a preview na auto-select — nem sempre a que você esperava. A doc declara o trade-off sem eufemismo: Vulkan 'may offer improved performance and better support for modern GPU features, but compatibility may vary depending on the system and drivers'.

## Como funciona
Em Preferences ‣ System ‣ Display Graphics: Backend escolhe a API por que a interface desenha ('Changing the backend requires restarting Blender'); Device Vulkan fixa o device de drawing para a UI — útil 'for systems with multiple GPUs (e.g., integrated + discrete)'. Para pipeline de estúdio, o ponto não é 'Vulkan é mais rápido': é registrar qual backend cada estação usa, porque bugs de driver são por-backend e os screenshots de comparação de look precisam da mesma configuração.

## Exemplo
Um laptop de revisão de corte alterna entre a iGPU (bateria) e a dGPU (tomada): Device Vulkan forçado na dGPU na estação, auto no modo bateria — o mesmo projeto, duas configurações documentadas.

## Limites e trade-offs
A doc não promete paridade de features de UI entre backends, e nota explicitamente que o hardware pode não suportar opções (algumas somem ou são corrigidas no start). Há dependências cruzadas documentadas no mesmo painel (ex.: certain shader-compile options exigem OpenGL) — os toggles interagem; teste combos antes de padronizar. Vulkan na interface é config de display, independente do render engine (Cycles/OptiX etc. têm sua própria seção no mesmo painel).

## Como verificar
Alterne o backend no host de teste, reinicie, e rode a mesma cena de viewport pesada com fps do overlay — comparação honesta é por máquina. Liste no doc de setup as opções que sumiram em cada backend (a própria doc avisa que unsupported ops desaparecem da UI). Reproduza no editor qualquer bug de flicker em ambos os backends antes de reportar — é a separação de culpas que o painel criou.

## Conexões
- [[blender-sequencer-cache-memoria-limites]] — Blender VSE: Memory Cache Limit vive nas Preferences, e o VSE lê dele.
- [[blender-limites-de-memoria-undo-shaders-stack]] — Blender 5.2: os limites de memória do System — undo, shaders, geometry nodes — e seus efeitos colaterais.

## Fontes
- [Blender — Preferences: System](https://docs.blender.org/manual/en/latest/editors/preferences/system.html) — a seção Display Graphics com Backend, Device Vulkan e a nota de reinicialização Consulta: 2026-10-04.
- [Blender — GPU Rendering (Cycles)](https://docs.blender.org/manual/en/latest/render/cycles/gpu_rendering.html) — a página de devices de render que a própria System referencia — o outro lado do GPU stack Consulta: 2026-10-04.
