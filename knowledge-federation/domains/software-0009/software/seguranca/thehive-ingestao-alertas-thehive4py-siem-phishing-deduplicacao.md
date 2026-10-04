---
id: software.seguranca.tranche06.000503
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

# TheHive: Ingestão Automatizada de Alertas via `TheHive4py` (`type`, `source`, `sourceRef`), Merge em Casos e Correlação de Observáveis

## Em uma frase
A biblioteca Python **`TheHive4py`** e o endpoint `/api/alert` permitem que SIEMs (Wazuh, Splunk, Elastic), coletores de caixas de denúncia de phishing (IMAP/Graph API) e sensores NIDS enviem alertas estruturados com observáveis anexados diretamente para o painel `Alerts` do TheHive.

## Por que importa
A chave primária de idempotência de um alerta no TheHive é a tupla **`(type, source, sourceRef)`**: se o script de integração gerar um `sourceRef` determinístico (como o ID único do alerta no SIEM ou o `Message-ID` do e-mail), reexecuções do script não criarão alertas duplicados.

## Como funciona
Ao revisar a fila de `Alerts`, o analista vê imediatamente se os observáveis contidos no novo alerta já apareceram em **casos anteriores ou em andamento** (*Similar Alerts / Cases*), podendo promover o alerta a um novo caso (`Import as new case`), mesclá-lo a uma investigação aberta (`Merge into existing case`) ou descartá-lo.

## Exemplo
```python
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact

hive = TheHiveApi("https://thehive.soc.internal.corp", "SIEM_FEEDER_KEY")
alert = Alert(
    title="Suricata ET MALWARE Cobalt Strike Beacon Detectado",
    tlp=2,
    severity=3,
    type="nids-alert",
    source="suricata-prod-sensor-01",
    sourceRef="suricata-eve-20261003-994812",
    description="Fluxo TLS suspeito para IP externo fora do padrao corporativo.",
    artifacts=[
        AlertArtifact(dataType="ip", data="198.51.100.214", ioc=True, tags=["c2-candidate"]),
        AlertArtifact(dataType="hostname", data="wkst-fin-09.internal.corp", ioc=False)
    ]
)
hive.create_alert(alert)
```

## Limites e trade-offs
Usar `uuid.uuid4()` aleatório no campo `sourceRef` a cada polling do SIEM desativa a proteção de deduplicação do TheHive e causa criação massiva de alertas repetidos caso o job de polling reprocessar a mesma janela de tempo.

## Como verificar
Submeta o mesmo objeto `Alert` duas vezes seguidas com idêntico `(type, source, sourceRef)` e confirme que a segunda chamada retorna erro HTTP `400/409` de alerta já existente.

## Conexões
- [[thehive-templates-casos-playbooks-padronizados-metricas-kpis]] — Veja também: TheHive: Padronização de Playbooks de Resposta a Incidentes com `Case Templates`, `Tasks` Obrigatórias e Métricas Customizadas.
- [[thehive-governanca-observables-tlp-pap-ioc-sighted-marking]] — Veja também: TheHive: Governança de `Observables` — Diferença Operacional entre **TLP** (*Traffic Light Protocol*) e **PAP** (*Permissible Actions Protocol*).
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.
- [[thehive-sincronizacao-bidirecional-misp-import-export-iocs]] — Referência cruzada direta com thehive-sincronizacao-bidirecional-misp-import-export-iocs.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
