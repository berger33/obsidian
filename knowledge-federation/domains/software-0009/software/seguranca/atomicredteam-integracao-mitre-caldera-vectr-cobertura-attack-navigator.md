---
id: software.seguranca.tranche12.001119
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

# Integração do **Atomic Red Team** com **MITRE Caldera**, **VECTR** e Camadas do **MITRE ATT&CK Navigator**

## Em uma frase
Embora o `Invoke-AtomicRedTeam` seja perfeito para executar testes individuais na linha de comando de um endpoint de laboratório, como orquestrar campanhas inteiras de testes atômicos remotamente em dezenas de máquinas, registrar os resultados de Red Team vs. Blue Team e gerar mapas de calor executivos no **MITRE ATT&CK Navigator**?

## Por que importa
Três integrações nativas resolvem esse desafio: **(1) Plugin `atomic` do MITRE Caldera** (`mitre/atomic`), que importa todos os mais de 1.870 testes do Atomic Red Team como *Abilities* prontas para serem executadas remotamente pelos agentes **Sandcat** do Caldera; **(2) Importação de logs ATTIRE no VECTR** (plataforma gratuita de gestão de Purple Team), que cruza os timestamps dos testes atômicos com os alertas do SIEM/EDR; e **(3) Geração de camadas JSON do ATT&CK Navigator**, colorindo cada técnica conforme o resultado do teste!

## Como funciona
Com essa arquitetura, a liderança de segurança visualiza claramente quais células da matriz MITRE ATT&CK foram testadas no trimestre, quais geraram bloqueio (verde), quais geraram apenas alerta (azul) e quais passaram despercebidas (vermelho)!

## Exemplo
```bash
# Gerar um resumo JSON da quantidade de testes atomicos disponiveis por tecnica MITRE ATT&CK para alimentar uma camada do Navigator
python3 - <<'PY'
import json, yaml
from pathlib import Path

scores = []
for yml in sorted(Path("atomic-red-team/atomics").glob("T*/T*.yaml")):
    data = yaml.safe_load(yml.read_text(encoding="utf-8"))
    tid = data.get("attack_technique")
    count = len(data.get("atomic_tests", []))
    scores.append({"techniqueID": tid, "score": count})
print(f"Total de tecnicas mapeadas: {len(scores)} (ex.: {scores[:3]})")
PY
```

## Limites e trade-offs
Ao planejar o calendário de testes atômicos do seu SOC, priorize as técnicas que combinam **alta prevalência real em incidentes** (relatórios anuais Red Canary Threat Detection Report / Mandiant M-Trends) com **baixa cobertura atual no seu ATT&CK Navigator**.

## Como verificar
Use sempre os GUIDs imutáveis (`auto_generated_guid`) ao vincular um teste atômico a um caso de teste no VECTR ou a uma regra Sigma.

## Conexões
- [[atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit]] — Veja também: Desenvolvimento e Validação de **Novos Testes Atômicos Corporativos**: Schema Validation, `pre-commit` e Boas Práticas de Autoria.
- [[atomicredteam-limites-testes-atomicos-variacoes-procedimento-evasao]] — Veja também: Limites dos Testes Atômicos: **Ancoragem em Procedimentos (*Procedure-Level Anchoring*)** e Como Evitar Regras Frágeis de Linha de Comando.
- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Referência cruzada direta com atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags]] — Referência cruzada direta com sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags.

## Fontes
- [Red Canary Atomic Red Team Official GitHub — Library of Tests Mapped to MITRE ATT&CK](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md) — repositório oficial do Atomic Red Team com mais de 1.870 testes atômicos declarativos em YAML mapeados às técnicas do MITRE ATT&CK; consultado em 2026-10-03.
- [Red Canary `Invoke-AtomicRedTeam` Official GitHub — PowerShell Execution Framework](https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/README.md) — documentação oficial do motor multiplataforma `Invoke-AtomicRedTeam` para Windows, Linux e macOS; consultado em 2026-10-03.
