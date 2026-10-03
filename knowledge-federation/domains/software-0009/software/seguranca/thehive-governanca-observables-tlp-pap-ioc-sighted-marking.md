---
id: software.seguranca.tranche06.000504
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md", "https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md", "https://github.com/TheHive-Project/cortex-analyzers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# TheHive: Governança de `Observables` — Diferença Operacional entre **TLP** (*Traffic Light Protocol*) e **PAP** (*Permissible Actions Protocol*)

## Em uma frase
No TheHive, cada observável adicionado a um caso possui dois controles independentes de segurança operacional (OPSEC): o **TLP** (*com quem a informação pode ser compartilhada*) e o **PAP** (*quais ações técnicas ativas o analista ou o Cortex podem executar com o indicador*).

## Por que importa
Um erro clássico de OPSEC em resposta a incidentes é submeter um arquivo de malware direcionado ou fazer `ping`/`curl`/consulta ativa ao domínio de Comando e Controle (C2) do atacante a partir de IPs públicos ou sandboxes abertos, avisando imediatamente o adversário de que ele foi descoberto.

## Como funciona
Enquanto `TLP:RED/AMBER/GREEN/WHITE` controla a divulgação, o **PAP** controla o contato com a infraestrutura adversária: **`PAP:RED`** permite apenas análise 100% passiva/offline em logs internos (proibindo tocar no servidor do atacante ou enviar para serviços em nuvem de terceiros); **`PAP:AMBER`** permite consultas passivas em bases reputacionais de terceiros (ex.: buscar o hash SHA-256 no VirusTotal sem fazer upload do binário); e **`PAP:GREEN`/`WHITE`** autoriza sondagem ativa.

## Exemplo
```python
from thehive4py.models import CaseObservable

# Cadastrar o binario suspeito com PAP:RED para impedir upload externo acidental para sandboxes na nuvem
obs = CaseObservable(
    dataType="hash",
    data="9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
    tlp=3,  # TLP:RED
    pap=2,  # PAP:AMBER (permite apenas consulta de hash, nunca upload do arquivo)
    ioc=True,
    sighted=True,
    tags=["targeted-implant", "no-cloud-upload"],
    message="Hash SHA-256 extraido da memoria RAM do servidor critico."
)
```

## Limites e trade-offs
Apenas adicionar um observável ao caso para investigação (ex.: o endereço IP do próprio servidor interno da empresa ou o e-mail da vítima) **não** o torna um IOC malicioso; marque a flag booleana **`ioc=True`** exclusivamente após confirmar que o artefato pertence à ameaça.

## Como verificar
Verifique na aba `Observables` do caso que apenas os artefatos confirmados como maliciosos possuem `ioc: true` antes de exportar o caso para o MISP.

## Conexões
- [[thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao]] — Veja também: TheHive: Ingestão Automatizada de Alertas via `TheHive4py` (`type`, `source`, `sourceRef`), Merge em Casos e Correlação de Observáveis.
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — Veja também: TheHive & Cortex: Análise em Escala de Observáveis com **Cortex Analyzers** e Guardrails Automáticos de `TLP`/`PAP`.
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — Referência cruzada direta com mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
