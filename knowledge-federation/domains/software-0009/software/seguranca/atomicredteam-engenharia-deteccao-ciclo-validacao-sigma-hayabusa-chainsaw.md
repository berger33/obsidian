---
id: software.seguranca.tranche12.001117
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

# Ciclo Completo de **Engenharia de Detecção (*Detection Engineering*)**: Executando Atomic Red Team e Validando com **Sigma, Hayabusa e Chainsaw**

## Em uma frase
Como construir um laboratório local de **Engenharia de Detecção** onde qualquer analista de segurança possa escrever uma nova regra **Sigma**, testar a técnica real e comprovar a detecção em menos de 3 minutos sem precisar de uma infraestrutura pesada de SIEM corporativo?

## Por que importa
O fluxo combina três ferramentas que já dominamos neste lote: **(1)** Em uma VM Windows de laboratório (com **Sysmon** e auditoria de linha de comando `4688` + PowerShell `4104` ativados), você executa o teste da técnica desejada via **`Invoke-AtomicTest`**; **(2)** Exporta os arquivos `.evtx` gerados em `C:\Windows\System32\winevt\Logs\`; e **(3)** Executa o **Hayabusa** ou o **Chainsaw (`chainsaw hunt -s ./minha-regra-sigma.yml`)** diretamente sobre os `.evtx` coletados!

## Como funciona
Se o Hayabusa e o Chainsaw dispararem o alerta esperado com os campos corretos no evento gerado pelo Atomic Red Team, você tem prova empírica de que a lógica da sua regra Sigma captura o artefato real produzido pelo Windows antes mesmo de convertê-la com `sigma convert` para o SIEM de produção!

## Exemplo
```bash
# Validar uma nova regra Sigma local contra os arquivos .evtx gerados apos a execucao de um teste do Atomic Red Team
chainsaw hunt ./evtx_pos_atomic_test/ \
  -s ./regras_em_desenvolvimento/proc_creation_win_t1053_schtasks.yml \
  --mapping ./chainsaw/mappings/sigma-event-logs-all.yml \
  --full
```

## Limites e trade-offs
Esse ciclo fechado (**Atomic Red Team -> `.evtx` -> Regra Sigma -> Chainsaw/Hayabusa**) também é a melhor forma de descobrir *bypasses* de regras Sigma (por exemplo, quando um teste atômico usa `/` em vez de `-` nas flags do Windows ou invoca um binário renomeado, exigindo o uso do modificador `|windash` ou `OriginalFileName` na regra Sigma!).

## Como verificar
Salve os recortes de `.evtx` gerados pelos testes atômicos (sem dados sensíveis) como **testes de regressão** das suas regras Sigma no repositório Git de Detection-as-Code.

## Conexões
- [[atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr]] — Veja também: Logging Estruturado de Execuções (`-ExecutionLogPath`), Módulos de Log Customizados (**Syslog, JSON, CSV, Attire**) e Correlação com o SIEM.
- [[atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit]] — Veja também: Desenvolvimento e Validação de **Novos Testes Atômicos Corporativos**: Schema Validation, `pre-commit` e Boas Práticas de Autoria.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx]] — Referência cruzada direta com chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx.
- [[sigma-pipeline-detection-as-code-cicd-validacao-schema-testes]] — Referência cruzada direta com sigma-pipeline-detection-as-code-cicd-validacao-schema-testes.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
