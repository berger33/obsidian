---
id: software.seguranca.tranche20.001912
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://theupdateframework.io/docs/metadata/", "https://github.com/theupdateframework/specification/blob/master/tuf-spec.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# The Update Framework (TUF): Usar limiar de assinatura na raiz

## Em uma frase
**The Update Framework (TUF) — Usar limiar de assinatura na raiz:** Root define chaves e threshold necessários para atualizar a própria raiz e outros papéis.

## Por que importa
O recorte de **usar limiar de assinatura na raiz** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar limiar de assinatura na raiz**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Configure custodiante independente para threshold de laboratório antes de publicar metadados. Teste em staging autorizado.

## Limites e trade-offs
Threshold mal escolhido pode permitir comprometimento ou bloquear recuperação legítima. Exceções exigem responsável e prazo.

## Como verificar
Teste atualização com número suficiente e insuficiente de assinaturas. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-impedir-rollback-por-versao-monotonica]] — Complementa o tópico com the update framework (tuf): impedir rollback por versão monotônica.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
