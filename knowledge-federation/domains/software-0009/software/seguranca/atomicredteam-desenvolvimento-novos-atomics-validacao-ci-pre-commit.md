---
id: software.seguranca.tranche12.001118
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

# Desenvolvimento e Validação de **Novos Testes Atômicos Corporativos**: Schema Validation, `pre-commit` e Boas Práticas de Autoria

## Em uma frase
Quando a sua equipe de Threat Intelligence descobre um novo procedimento de ataque usado por um grupo de ransomware contra o seu setor (por exemplo, o abuso de um utilitário legítimo específico de backup ou RMM usado na sua empresa), você não precisa esperar que alguém o publique na internet: você pode codificá-lo como um **Teste Atômico interno** seguindo o mesmo padrão de qualidade do repositório oficial da Red Canary!

## Por que importa
O repositório do Atomic Red Team utiliza hooks do **`pre-commit`** e pipelines de validação que verificam automaticamente a conformidade sintática de cada arquivo `Txxxx.yaml`, a unicidade dos `auto_generated_guid`, a correspondência de todos os `#{argumentos}` declarados em `input_arguments` com os argumentos usados nos blocos `executor.command` e `cleanup_command`, e a codificação correta (incluindo Byte Order Marks em scripts PowerShell)!

## Como funciona
Seguindo essa mesma disciplina no repositório interno do seu Purple Team, você garante que todos os testes customizados criados pelos seus engenheiros possam ser executados sem erro tanto pelo `Invoke-AtomicRedTeam` quanto pelo **MITRE Caldera**!

## Exemplo
```bash
# Instalar e executar os hooks de validacao pre-commit em um repositorio de testes atomicos customizados
pip3 install pre-commit
pre-commit install
pre-commit run --all-files
```

## Limites e trade-offs
Três princípios de design de um excelente teste atômico: **(1) Atomicidade** (teste apenas *uma* técnica ou variação específica por entrada, sem encadear 5 etapas de ataque no mesmo bloco); **(2) Determinismo** (não dependa de serviços externos instáveis na internet); e **(3) Segurança por padrão** (use payloads benignos como `calc.exe`, `whoami` ou arquivos de texto dummy em vez de binários destrutivos).

## Como verificar
Gere automaticamente a documentação Markdown (`Txxxx.md`) a partir dos arquivos `Txxxx.yaml` na sua pipeline de CI para facilitar a revisão por analistas do SOC.

## Conexões
- [[atomicredteam-engenharia-deteccao-ciclo-validacao-sigma-hayabusa-chainsaw]] — Veja também: Ciclo Completo de **Engenharia de Detecção (*Detection Engineering*)**: Executando Atomic Red Team e Validando com **Sigma, Hayabusa e Chainsaw**.
- [[atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator]] — Veja também: Integração do **Atomic Red Team** com **MITRE Caldera**, **VECTR** e Camadas do **MITRE ATT&CK Navigator**.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup]] — Referência cruzada direta com atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup.
- [[sigma-pipeline-detection-as-code-cicd-validacao-schema-testes]] — Referência cruzada direta com sigma-pipeline-detection-as-code-cicd-validacao-schema-testes.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
