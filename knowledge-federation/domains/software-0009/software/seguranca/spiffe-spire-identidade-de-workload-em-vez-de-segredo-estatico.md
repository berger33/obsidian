---
id: software.seguranca.tranche19.001801
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

# SPIFFE/SPIRE: Identidade de workload em vez de segredo estático

## Em uma frase
**SPIFFE/SPIRE — Identidade de workload em vez de segredo estático:** SPIFFE atribui identidade criptográfica a workloads e SPIRE pode emitir credenciais de curta duração após atestação.

## Por que importa
O recorte de **identidade de workload em vez de segredo estático** ajuda a substituir credenciais estáticas por identidade de workload verificável, com emissão e rotação automatizadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **identidade de workload em vez de segredo estático**, SPIRE atesta nós e workloads e emite SVIDs associados ao trust domain; consumidores validam identidade e trust bundle. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em laboratório, valide que um serviço recebe identidade do workload sem copiar uma chave privada para a imagem. Teste em staging autorizado.

## Limites e trade-offs
Uma identidade autenticada não decide quais operações o serviço pode executar. Exceções exigem responsável e prazo.

## Como verificar
Inspecione SVID, trust domain e principal vistos pelo consumidor e teste uma identidade não autorizada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[spiffe-spire-nomear-e-isolar-trust-domains]] — Complementa o tópico com spiffe/spire: nomear e isolar trust domains.

## Fontes
- [SPIRE — Concepts](https://spiffe.io/docs/latest/spire-about/spire-concepts/) — documentação oficial de trust domains, agents, attestation, SVIDs e bundles; consultado em 2026-10-04.
- [SPIRE — Configuration](https://spiffe.io/docs/latest/deploying/configuring/) — guia oficial de configuração de servidores, agents, attestors e workload registration; consultado em 2026-10-04.
