---
id: software.seguranca.tranche12.001113
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md", "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Motor de Execução **`Invoke-AtomicRedTeam`** (PowerShell Core Multiplataforma): `-ShowDetails`, `-CheckPrereqs`, `-GetPrereqs` e `-Cleanup`

## Em uma frase
Embora os arquivos YAML do Atomic Red Team possam ser lidos manualmente, o módulo oficial **`Invoke-AtomicRedTeam`** (compatível com **Windows PowerShell 5.1** e **PowerShell Core `pwsh` 7+ no Linux, macOS e Windows**) automatiza todo o ciclo de vida de inspeção, preparação de pré-requisitos, execução, logging e limpeza de cada técnica!

## Por que importa
Para operar com segurança em um exercício de Purple Team, nunca execute um teste às cegas: siga sempre o fluxo de 4 etapas do `Invoke-AtomicTest`: **(1) Inspecionar** o que o teste fará (`-ShowDetailsBrief` ou `-ShowDetails`), **(2) Verificar e instalar pré-requisitos** (`-CheckPrereqs` e `-GetPrereqs`), **(3) Executar o teste** (por número `-TestNumbers`, nome `-TestNames` ou GUID `-TestGuids`) e **(4) Reverter o estado da máquina** (`-Cleanup`)!

## Como funciona
Você também pode sobrescrever qualquer argumento de entrada (`input_arguments`) em tempo de execução passando uma *hashtable* PowerShell para o parâmetro **`-InputArgs`**!

## Exemplo
```powershell
# Fluxo seguro de 4 etapas no PowerShell (Windows/Linux/macOS) com Invoke-AtomicTest para a tecnica T1053.005
Invoke-AtomicTest T1053.005 -ShowDetailsBrief
Invoke-AtomicTest T1053.005 -TestNumbers 1 -CheckPrereqs
Invoke-AtomicTest T1053.005 -TestNumbers 1
Invoke-AtomicTest T1053.005 -TestNumbers 1 -Cleanup
```

## Limites e trade-offs
Se o EDR da máquina de laboratório bloquear o download da pasta `atomics/` (porque os YAMLs e binários auxiliares em `ExternalPayloads` contêm assinaturas conhecidas de ferramentas ofensivas), configure uma exclusão de caminho apenas para o diretório de instalação (`C:\AtomicRedTeam\`), mantendo a proteção ativa para a execução real dos processos!

## Como verificar
Use `-PathToAtomicsFolder` caso você mantenha um repositório Git interno customizado de testes atômicos fora do caminho padrão.

## Conexões
- [[atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup]] — Veja também: Anatomia da Especificação YAML de um Teste Atômico: **`auto_generated_guid`**, **`input_arguments`**, **`dependencies`**, **`executor`** e **`cleanup_command`**.
- [[atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr]] — Veja também: Emulação de Adversários em **Linux, macOS e Containers** com Atomic Red Team: Persistência (`systemd`/`cron`), Credenciais e Escape de Container.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr]] — Referência cruzada direta com atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
