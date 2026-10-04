---
id: software.seguranca.tranche06.000508
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

# Cortex: Desenvolvimento de `Analyzers` e `Responders` Customizados em Python (`cortexutils`) e Isolamento em Containers Docker

## Em uma frase
Quando o SOC precisa consultar bancos de dados internos (CMDB de ativos, logs de DHCP/VPN corporativos, diretório interno de funcionários) ou acionar APIs proprietárias durante um incidente, o **Cortex** permite criar *Analyzers* e *Responders* customizados em Python usando o SDK **`cortexutils`**.

## Por que importa
Um *Analyzer* interno de CMDB que responde instantaneamente *"a quem pertence esta estação de trabalho, qual o departamento do usuário e se o servidor é de produção Tier 1"* economiza dezenas de minutos de triagem em cada alerta.

## Como funciona
Cada módulo customizado consiste em um arquivo descritor JSON (definindo `name`, `version`, `dataTypeList`, `baseConfig`, `configurationItems`) e um script executável que herda de `cortexutils.analyzer.Analyzer` (implementando `summary()`, `artifacts()` e `run()`) ou `cortexutils.responder.Responder`, empacotado preferencialmente como imagem Docker isolada executada pelo *Job Runner* do Cortex.

## Exemplo
```python
#!/usr/bin/env python3
from cortexutils.analyzer import Analyzer

class InternalCmdbLookupAnalyzer(Analyzer):
    def summary(self, raw):
        taxonomies = []
        level = "warning" if raw.get("criticality") == "tier-0" else "info"
        taxonomies.append(self.build_taxonomy(level, "CMDB", "Criticality", raw.get("criticality", "unknown")))
        return {"taxonomies": taxonomies}

    def run(self):
        hostname = self.get_data()
        asset_info = {"hostname": hostname, "owner": "secops@internal.corp", "criticality": "tier-0"}
        self.report(asset_info)

if __name__ == "__main__":
    InternalCmdbLookupAnalyzer().run()
```

## Limites e trade-offs
O método `summary()` retorna **Taxonomies** curtas coloridas (`info`, `safe`, `suspicious`, `malicious`) que aparecem diretamente como *badges* ao lado do observável no TheHive sem que o analista precise abrir o JSON completo do relatório.

## Como verificar
Rode o Analyzer customizado passando um JSON de entrada via `stdin` em teste local e valide que a saída contém `{"success": true, "summary": {"taxonomies": [...]}}`.

## Conexões
- [[thehive-sincronizacao-bidirecional-misp-import-export-iocs]] — Veja também: TheHive: Integração Bidirecional com o **MISP** (Importação Filtrada de Eventos para Alertas e Exportação de IOCs Confirmados).
- [[thehive-templates-relatorios-curtos-longos-fusao-casos]] — Veja também: TheHive: Customização de `Report Templates` do Cortex (Short / Long Reports), Fusão de Casos (`Case Merging`) e Fechamento Auditável.
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — Referência cruzada direta com thehive-orquestracao-cortex-analyzers-tlp-pap-opsec.
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — Referência cruzada direta com thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
