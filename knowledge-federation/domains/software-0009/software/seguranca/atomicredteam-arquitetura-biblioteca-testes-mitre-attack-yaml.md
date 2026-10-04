---
id: software.seguranca.tranche12.001111
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

# Arquitetura do **Atomic Red Team (`redcanaryco/atomic-red-team`)**: Biblioteca Aberta de Testes Determinísticos Mapeados ao **MITRE ATT&CK**

## Em uma frase
Como uma equipe de Engenharia de Detecção (Blue Team / SOC) pode provar cientificamente que o seu EDR, SIEM e conjunto de regras Sigma realmente detectam uma técnica do **MITRE ATT&CK** (como *OS Credential Dumping: LSASS Memory `T1003.001`* ou *Scheduled Task `T1053.005`*), em vez de apenas confiar nas promessas de marketing do fabricante?

## Por que importa
Criado pela **Red Canary** e mantido por uma comunidade global de pesquisadores, o **Atomic Red Team** é a maior biblioteca open-source de **testes de emulação de adversários pequenos, portáteis, determinísticos e reproduzíveis ("testes atômicos")**, com mais de **1.870 testes** organizados diretamente pelo ID da técnica ou subtécnica do **MITRE ATT&CK** (`atomics/Txxxx.xxx/Txxxx.xxx.yaml`)!

## Como funciona
Cada arquivo YAML de técnica define uma lista de `atomic_tests` autocontidos: cada teste especifica um **`auto_generated_guid`** único e imutável, **`supported_platforms`** (`windows`, `linux`, `macos`, `iaas:aws`, `azure-ad`, `containers`, `office-365`, `google-workspace`), **`input_arguments`** parametrizáveis, verificações e instaladores de pré-requisitos (**`dependencies`**), o comando de ataque (**`executor`**) e o comando de reversão (**`cleanup_command`**)!

## Exemplo
```bash
# Clonar o repositorio oficial do Atomic Red Team e inspecionar a definicao YAML da subtecnica T1003.001 (LSASS Memory)
git clone --depth 1 https://github.com/redcanaryco/atomic-red-team.git
ls -la atomic-red-team/atomics/T1003.001/
head -n 45 atomic-red-team/atomics/T1003.001/T1003.001.yaml
```

## Limites e trade-offs
Por que o formato declarativo YAML do Atomic Red Team se tornou o padrão da indústria? Porque os testes podem ser executados tanto **manualmente** (copiando o comando do arquivo `.md` gerado para cada técnica) quanto de forma **100% automatizada** por múltiplos motores de execução (como **`Invoke-AtomicRedTeam`** em PowerShell, **`atomic-operator`** em Python ou o plugin **`atomic`** dentro do **MITRE Caldera**)!

## Como verificar
Execute sempre testes do Atomic Red Team apenas em máquinas de laboratório ou endpoints de homologação dedicados e com autorização formal documentada.

## Conexões
- [[atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup]] — Veja também: Anatomia da Especificação YAML de um Teste Atômico: **`auto_generated_guid`**, **`input_arguments`**, **`dependencies`**, **`executor`** e **`cleanup_command`**.
- [[atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs]] — Referência cruzada direta com atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs.
- [[sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags]] — Referência cruzada direta com sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
