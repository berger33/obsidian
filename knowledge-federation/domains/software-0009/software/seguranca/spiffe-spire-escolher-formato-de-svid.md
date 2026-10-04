---
id: software.seguranca.tranche19.001807
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://spiffe.io/docs/latest/spire-about/spire-concepts/", "https://spiffe.io/docs/latest/deploying/configuring/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SPIFFE/SPIRE: Escolher formato de SVID

## Em uma frase
**SPIFFE/SPIRE — Escolher formato de SVID:** X.509-SVID e JWT-SVID oferecem formatos de credencial distintos para protocolos e consumidores diferentes.

## Por que importa
O recorte de **escolher formato de svid** ajuda a substituir credenciais estáticas por identidade de workload verificável, com emissão e rotação automatizadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher formato de svid**, SPIRE atesta nós e workloads e emite SVIDs associados ao trust domain; consumidores validam identidade e trust bundle. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use X.509-SVID em canal TLS de serviço no teste e valide cadeia e identidade no peer. Teste em staging autorizado.

## Limites e trade-offs
JWT-SVID pode ser enviado como bearer token e requer atenção a audiência, expiração e replay. Exceções exigem responsável e prazo.

## Como verificar
Verifique tipo, audience quando aplicável, validade e processo de rotação no cliente real. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[spiffe-spire-distribuir-trust-bundles-com-rotacao]] — Complementa o tópico com spiffe/spire: distribuir trust bundles com rotação.

## Fontes
- [SPIRE — Concepts](https://spiffe.io/docs/latest/spire-about/spire-concepts/) — documentação oficial de trust domains, agents, attestation, SVIDs e bundles; consultado em 2026-10-04.
- [SPIRE — Configuration](https://spiffe.io/docs/latest/deploying/configuring/) — guia oficial de configuração de servidores, agents, attestors e workload registration; consultado em 2026-10-04.
