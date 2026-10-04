---
id: software.seguranca.tranche13.001226
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

# Análise Dinâmica com o `capa`: Extraindo Capacidades de Relatórios de **Sandboxes (`CAPE`, `DRAKVUF`, `VMRay`)** e Filtrando por **PID (`--restrict-to-processes`)**

## Em uma frase
O que fazer quando uma amostra de ransomware ou loader avançado está pesadamente empacotada (*packed* com VMProtect/Themida) ou criptografada, fazendo com que a análise estática do arquivo em disco veja apenas o *stub* do empacotador?

## Por que importa
A partir do **capa v7+**, a Mandiant introduziu o suporte completo a **Análise Dinâmica sobre Traces de Execução de Sandboxes**! Você detona o binário empacotado em uma sandbox de análise de malware — como o **CAPE Sandbox** (open-source), o **DRAKVUF** (baseado em hipervisor Xen sem agente interno!) ou o **VMRay** — exporta o relatório de execução (que contém o log cronológico completo de todas as chamadas de API do sistema operacional, argumentos passados e processos filhos criados durante a execução real!) e passa esse relatório diretamente para o **`capa`**!

## Como funciona
O `capa` avalia as regras nos escopos dinâmicos **`process`**, **`thread`**, **`span of calls`** (sequência de chamadas de API próximas dentro da mesma thread) e **`call`**, revelando todas as capacidades reais do malware mesmo que o binário original estivesse 100% ofuscado em disco!

## Exemplo
```bash
# Analisar o relatorio JSON de execucao dinamica de uma sandbox CAPE restringindo a analise apenas ao PID do processo malicioso injetado
capa \
  --restrict-to-processes 3840,4112 \
  -v ./sandbox_reports/cape_report_ransomware.json
```

## Limites e trade-offs
Em relatórios de sandbox grandes (que capturam também processos de fundo do Windows como `explorer.exe` ou `svchost.exe`), utilize sempre a flag **`--restrict-to-processes <PID1,PID2>`** do `capa` para focar a avaliação de regras exclusivamente nos Process IDs (`PID`) da cadeia de execução do malware — reduzindo drasticamente o tempo de análise e o consumo de memória RAM!

## Como verificar
Essa unificação estática + dinâmica sob a mesma linguagem de regras `capa-rules` permite que o time de Threat Intelligence escreva **uma única regra YAML** que funciona tanto no arquivo PE em disco quanto no trace JSON da sandbox CAPE!

## Conexões
- [[capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt]] — Veja também: Análise Multi-Formato no `capa`: Executáveis **Windows PE**, **Linux ELF**, Assemblies **.NET (CIL)**, **Shellcode Bruto (`-f sc32`/`sc64`)** e Assinaturas **FLIRT (`-s`)**.
- [[capa-integracao-ida-pro-ghidra-binary-ninja-capa-explorer-web]] — Veja também: Integração do `capa` com **Ghidra, IDA Pro, Binary Ninja** e **`capa Explorer Web`**: Navegação Interativa e Renomeação de Funções na Engenharia Reversa.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.
- [[capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction]] — Referência cruzada direta com capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
