---
id: software.seguranca.tranche13.001221
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/capa/master/README.md", "https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **Mandiant `capa` (`mandiant/capa`)**: Detecção Automatizada de Capacidades em Binários (**PE, ELF, .NET, Shellcode**) Mapeadas ao **MITRE ATT&CK** e **MBC**

## Em uma frase
Quando um analista de malware ou engenheiro de resposta a incidentes (DFIR / SOC) recebe um executável suspeito desconhecido (que não bate com nenhuma assinatura de antivírus convencional), como descobrir em **segundos** *o que aquele binário é capaz de fazer* — por exemplo, se ele instala um serviço, injeta código em outro processo, cifra arquivos com AES/ChaCha20, abre um backdoor reverso ou detecta máquinas virtuais — **antes mesmo de abrir o Ghidra ou o IDA Pro**?

## Por que importa
Desenvolvido pela equipe **FLARE da Mandiant (Google Cloud Security)**, o **`capa`** é a ferramenta open-source padrão mundial para **identificação automatizada de capacidades comportamentais e estruturais em programas executáveis**!

## Como funciona
O `capa` desmonta e analisa a estrutura de controle de fluxo (*Control Flow Graph* — CFG), instruções de assembly, chamadas de API, constantes, strings e imports de binários **Windows PE (x86/x64)**, **Linux ELF**, **módulos .NET (CIL)**, **Shellcodes brutos** e até **relatórios dinâmicos de Sandboxes (CAPE, DRAKVUF, VMRay)**, avaliando centenas de regras YAML oficiais (`capa-rules`) e gerando uma matriz imediata mapeada para o **MITRE ATT&CK** e para o **Malware Behavior Catalog (`MBC`)**!

## Exemplo
```bash
# Analisar um binario suspeito com o Mandiant capa exibindo a matriz automatica de ATT&CK Tactics, MBC Objectives e Capabilities
capa ./amostras/suspicious_loader.exe
```

## Limites e trade-offs
Ao contrário do **YARA** (que busca padrões de bytes ou strings na superfície do arquivo inteiro), o **`capa` raciocina sobre a semântica da engenharia reversa por escopo** (`file`, `function`, `basic block`, `instruction`): uma regra do `capa` pode exigir que *dentro da mesma função* exista um loop que faz `XOR` com uma constante `0x5A` e logo em seguida chame `VirtualAlloc` + `CreateThread`!

## Como verificar
Se o binário estiver empacotado (*packed*, ex.: UPX, Themida, VMProtect), o `capa` detecta automaticamente a limitação de código visível e alerta o analista para desempacotar a amostra ou passar o relatório de execução dinâmica da sandbox!

## Conexões
- [[capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao]] — Veja também: Triagem Rápida vs. Engenharia Reversa Profunda no `capa`: Modos Padrão, Verboso (**`-v`**), Muito Verboso (**`-vv`**) e Exportação **`-j` JSON**.
- [[capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction]] — Referência cruzada direta com capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
