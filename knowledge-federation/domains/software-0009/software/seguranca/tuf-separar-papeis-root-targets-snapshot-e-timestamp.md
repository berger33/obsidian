---
id: software.seguranca.tranche20.001911
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

# The Update Framework (TUF): Separar papéis Root, Targets, Snapshot e Timestamp

## Em uma frase
**The Update Framework (TUF) — Separar papéis Root, Targets, Snapshot e Timestamp:** Papéis de metadados distribuem chaves e responsabilidades diferentes no fluxo de verificação.

## Por que importa
O recorte de **separar papéis root, targets, snapshot e timestamp** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar papéis root, targets, snapshot e timestamp**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Desenhe trust graph de um repositório de atualização antes de configurar client. Teste em staging autorizado.

## Limites e trade-offs
Uma assinatura válida de Targets não substitui verificação de frescor de Timestamp e Snapshot. Exceções exigem responsável e prazo.

## Como verificar
Teste cada papel isoladamente e confirme sequência de verificação no cliente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-usar-limiar-de-assinatura-na-raiz]] — Complementa o tópico com the update framework (tuf): usar limiar de assinatura na raiz.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
