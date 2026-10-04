---
id: software.seguranca.tranche19.001885
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

# External Secrets Operator: Escolher refreshInterval e estratégia

## Em uma frase
**External Secrets Operator — Escolher refreshInterval e estratégia:** ExternalSecret reconcilia fonte segundo intervalo e política de refresh configurados.

## Por que importa
O recorte de **escolher refreshinterval e estratégia** ajuda a reduzir duplicação manual de credenciais e separar fonte de segredo das aplicações consumidoras. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher refreshinterval e estratégia**, ExternalSecret referencia SecretStore ou ClusterSecretStore, lê provider remoto e reconcilia o Secret alvo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use intervalo compatível com cadência de rotação e carga do provider em laboratório. Teste em staging autorizado.

## Limites e trade-offs
Refresh lento prolonga uso de valor antigo; refresh agressivo aumenta chamadas e risco de quota. Exceções exigem responsável e prazo.

## Como verificar
Altere segredo canário no backend e meça quando Secret Kubernetes é atualizado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[external-secrets-tratar-criacao-e-delecao-do-secret-alvo]] — Complementa o tópico com external secrets operator: tratar criação e deleção do secret alvo.

## Fontes
- [External Secrets Operator — Google Secret Manager](https://external-secrets.io/latest/provider/google-secrets-manager/) — guia oficial de provider, autenticação e SecretStore para Google Secret Manager; consultado em 2026-10-04.
- [External Secrets Operator — ClusterSecretStore API](https://github.com/external-secrets/external-secrets/blob/main/docs/api/clustersecretstore.md) — referência oficial de escopo e configuração de ClusterSecretStore; consultado em 2026-10-04.
