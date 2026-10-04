---
id: software.seguranca.tranche12.001116
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

# Logging Estruturado de Execuções (`-ExecutionLogPath`), Módulos de Log Customizados (**Syslog, JSON, CSV, Attire**) e Correlação com o SIEM

## Em uma frase
Quando você executa uma bateria de 50 testes do Atomic Red Team em uma máquina de laboratório, como saber exatamente em qual segundo cada teste começou, qual comando exato rodou, qual foi o `ProcessId` (PID) do processo criado, qual usuário executou e qual `auto_generated_guid` deve ser correlacionado com os alertas do SIEM?

## Por que importa
O `Invoke-AtomicRedTeam` grava por padrão um log detalhado de todas as execuções e suporta a flag **`-ExecutionLogPath`** e **`-LoggingModule`** — incluindo o **`Attire-ExecutionLogger`**, que gera arquivos JSON padronizados no formato **ATTIRE (*Attack Execution Plan and Results*)**, contendo o timestamp exato de início/fim (`time-start`, `time-stop`), o ID da técnica MITRE, o GUID do teste, a linha de comando executada e a saída (`stdout`/`stderr`)!

## Como funciona
Ao ingerir esse log de execução CSV/JSON/ATTIRE no seu SIEM (ou cruzá-lo via script Python com os alertas gerados pelo seu EDR, Hayabusa ou Chainsaw), você calcula automaticamente a **taxa de cobertura real (% de testes detectados vs. bloqueados vs. invisíveis)**!

## Exemplo
```powershell
# Executar uma bateria de testes atomicos gravando o log estruturado no formato JSON ATTIRE para correlacao automatica com o SIEM
Invoke-AtomicTest T1003.001 -TestNumbers 1,2 `
  -LoggingModule "Attire-ExecutionLogger" `
  -ExecutionLogPath "./logs_purple_team/execucao_t1003_attire.json"
```

## Limites e trade-offs
Incluir o **`ProcessId` (PID)** e o timestamp UTC com precisão de milissegundos no log do `Invoke-AtomicTest` elimina falsas correlações durante o exercício de Purple Team, garantindo que o alerta do SIEM foi realmente causado pelo processo do teste atômico e não por uma atividade de fundo do sistema operacional.

## Como verificar
Archive os logs JSON `Attire-ExecutionLogger` de cada campanha mensal de validação de detecção para acompanhar a evolução histórica da cobertura MITRE ATT&CK do seu SOC.

## Conexões
- [[atomicredteam-testes-cloud-aws-azure-ad-gcp-m365-identidade]] — Veja também: Testes Atômicos de **Nuvem e Identidade** (`iaas:aws`, `iaas:azure`, `iaas:gcp`, `azure-ad`, `office-365`, `google-workspace`).
- [[atomicredteam-engenharia-deteccao-ciclo-validacao-sigma-hayabusa-chainsaw]] — Veja também: Ciclo Completo de **Engenharia de Detecção (*Detection Engineering*)**: Executando Atomic Red Team e Validando com **Sigma, Hayabusa e Chainsaw**.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs]] — Referência cruzada direta com atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
