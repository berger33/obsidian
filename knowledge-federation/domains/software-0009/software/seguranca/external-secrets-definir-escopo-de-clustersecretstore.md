---
id: software.seguranca.tranche19.001884
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
fontes: ["https://external-secrets.io/latest/provider/google-secrets-manager/", "https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# External Secrets Operator: Definir escopo de ClusterSecretStore

## Em uma frase
**External Secrets Operator — Definir escopo de ClusterSecretStore:** Campos de condições podem limitar namespaces que podem usar um ClusterSecretStore.

## Por que importa
O recorte de **definir escopo de clustersecretstore** ajuda a reduzir duplicação manual de credenciais e separar fonte de segredo das aplicações consumidoras. A equipe registra risco, evidência e responsável.

## Como funciona
Para **definir escopo de clustersecretstore**, ExternalSecret referencia SecretStore ou ClusterSecretStore, lê provider remoto e reconcilia o Secret alvo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita somente namespaces `payments-staging` e `billing-staging` durante validação. Teste em staging autorizado.

## Limites e trade-offs
Uma condição aberta pode transformar store compartilhado em caminho de exfiltração entre equipes. Exceções exigem responsável e prazo.

## Como verificar
Tente referenciar o store de namespace permitido e não permitido. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[external-secrets-escolher-refreshinterval-e-estrategia]] — Complementa o tópico com external secrets operator: escolher refreshinterval e estratégia.

## Fontes
- [External Secrets Operator — Google Secret Manager](https://external-secrets.io/latest/provider/google-secrets-manager/) — guia oficial de provider, autenticação e SecretStore para Google Secret Manager; consultado em 2026-10-04.
- [External Secrets Operator — ClusterSecretStore API](https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md) — referência oficial de escopo e configuração de ClusterSecretStore; consultado em 2026-10-04.
