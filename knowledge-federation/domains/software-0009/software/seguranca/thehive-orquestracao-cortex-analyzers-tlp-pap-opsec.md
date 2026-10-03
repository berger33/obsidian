---
id: software.seguranca.tranche06.000505
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

# TheHive & Cortex: Análise em Escala de Observáveis com **Cortex Analyzers** e Guardrails Automáticos de `TLP`/`PAP`

## Em uma frase
**Cortex** (`TheHive-Project/Cortex`) é o motor de análise e resposta ativa que acompanha o TheHive e o MISP, permitindo executar mais de 100 **Analyzers** (VirusTotal, AbuseIPDB, Shodan, GreyNoise, PassiveTotal, YARA, CAPEv2, Joe Sandbox, MaxMind, DNS/WHOIS) sobre observáveis individuais ou em lote via uma única API.

## Por que importa
Em vez de o analista abrir 15 abas no navegador e copiar chaves de API manualmente para consultar a reputação de 50 IPs e domínios de um incidente, o Cortex executa todos os *Analyzers* em paralelo dentro de containers Docker ou ambientes Python/Linux isolados e devolve o relatório padronizado.

## Como funciona
Crucialmente, cada *Analyzer* no Cortex possui configurações explícitas de **`tlp` máximo** e **`pap` máximo** permitidos: por exemplo, o analyzer `VirusTotal_Scan_3_0` (que faz upload do arquivo) é configurado para exigir `TLP <= GREEN` e `PAP <= GREEN`, enquanto `VirusTotal_GetReport_3_0` (que consulta apenas o hash) aceita `TLP <= AMBER` e `PAP <= AMBER`. Se um analista tentar rodar o upload em um arquivo `TLP:RED`, o próprio Cortex **bloqueia a execução automaticamente**.

## Exemplo
```bash
# Disparar um job de analise passiva no Cortex via API REST para um observavel de IP
curl -sS -X POST "https://cortex.soc.internal.corp/api/analyzer/AbuseIPDB_1_0/run" \
  -H "Authorization: Bearer ${CORTEX_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": "198.51.100.214",
    "dataType": "ip",
    "tlp": 2,
    "pap": 2
  }' | jq .
```

## Limites e trade-offs
Configure sempre no Cortex os limites `auto_extract_artifacts` e verifique os tetos de `tlp`/`pap` de cada Analyzer externo antes de liberar chaves de API comerciais para a equipe de Nível 1 do SOC.

## Como verificar
Tente executar um Analyzer restrito a `TLP:GREEN` contra um observável marcado como `TLP:RED` (`tlp: 3`) e confirme que o Cortex recusa o job por violação de política OPSEC.

## Conexões
- [[thehive-governanca-observables-tlp-pap-ioc-sighted-marking]] — Veja também: TheHive: Governança de `Observables` — Diferença Operacional entre **TLP** (*Traffic Light Protocol*) e **PAP** (*Permissible Actions Protocol*).
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — Veja também: TheHive & Cortex: Contenção e Resposta Ativa a Incidentes com **Cortex Responders** (Isolamento EDR, Bloqueio Firewall/RPZ e Revogação IAM).
- [[thehive-desenvolvimento-analyzers-customizados-cortexutils-docker]] — Referência cruzada direta com thehive-desenvolvimento-analyzers-customizados-cortexutils-docker.
- [[capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp]] — Referência cruzada direta com capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
