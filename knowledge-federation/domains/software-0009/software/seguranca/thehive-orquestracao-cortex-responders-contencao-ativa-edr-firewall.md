---
id: software.seguranca.tranche06.000506
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

# TheHive & Cortex: Contenção e Resposta Ativa a Incidentes com **Cortex Responders** (Isolamento EDR, Bloqueio Firewall/RPZ e Revogação IAM)

## Em uma frase
Além dos *Analyzers* (que leem e enriquecem dados), o Cortex executa **Responders** — módulos de ação ativa que podem ser disparados a partir de um `Case`, `Alert`, `Task` ou `Observable` no TheHive para conter ameaças em segundos.

## Por que importa
Durante um ataque de ransomware ou exfiltração ativa, permite ao analista clicar em *Run Responder* diretamente sobre o observável de hostname/IP/usuário no TheHive para isolar a máquina no EDR (Velociraptor, CrowdStrike, Defender), bloquear o domínio no firewall/DNS RPZ ou revogar sessões OIDC no IdP.

## Como funciona
Cada execução de *Responder* fica registrada na aba `Responders` do caso com o usuário que disparou a ação, o carimbo de tempo, os parâmetros enviados e o status de retorno (`Success` / `Failure`), além de poder adicionar automaticamente tags ao observável (ex.: `action:blocked-on-firewall` ou `host:isolated`).

## Exemplo
```bash
# Acionar um Responder do Cortex via API para bloquear um IP de C2 confirmado na borda
curl -sS -X POST "https://cortex.soc.internal.corp/api/responder/FirewallBlockIP_1_0/run" \
  -H "Authorization: Bearer ${CORTEX_Responder_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "dataType": "thehive:case_artifact",
    "data": {
      "dataType": "ip",
      "data": "198.51.100.214",
      "ioc": true,
      "tlp": 2
    }
  }' | jq .
```

## Limites e trade-offs
Um *Responder* que bloqueia IPs no firewall ou isola servidores em produção pode causar indisponibilidade severa se disparado contra o IP de um gateway interno ou servidor DNS corporativo; valide sempre o alvo contra uma *allowlist* de infraestrutura crítica dentro do código do Responder.

## Como verificar
Execute o Responder em ambiente de homologação contra um IP de teste e verifique que o status retorna `Success` e que a tag de bloqueio é anexada ao artefato no TheHive.

## Conexões
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — Veja também: TheHive & Cortex: Análise em Escala de Observáveis com **Cortex Analyzers** e Guardrails Automáticos de `TLP`/`PAP`.
- [[thehive-sincronizacao-bidirecional-misp-import-export-iocs]] — Veja também: TheHive: Integração Bidirecional com o **MISP** (Importação Filtrada de Eventos para Alertas e Exportação de IOCs Confirmados).
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
