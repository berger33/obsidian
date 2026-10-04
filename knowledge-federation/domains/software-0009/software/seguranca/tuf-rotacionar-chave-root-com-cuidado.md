---
id: software.seguranca.tranche20.001918
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

# The Update Framework (TUF): Rotacionar chave Root com cuidado

## Em uma frase
**The Update Framework (TUF) — Rotacionar chave Root com cuidado:** Atualização de Root pode exigir assinaturas da raiz atual e da nova para manter cadeia de confiança.

## Por que importa
O recorte de **rotacionar chave root com cuidado** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **rotacionar chave root com cuidado**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Planeje rotação em repositório descartável e distribua metadados de transição em ordem. Teste em staging autorizado.

## Limites e trade-offs
Remover chave antiga antes da adoção da nova pode deixar clientes sem trust path. Exceções exigem responsável e prazo.

## Como verificar
Atualize client incrementalmente e verifique que ele rejeita root sem threshold. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-confiar-em-mirrors-sem-ceder-verificacao]] — Complementa o tópico com the update framework (tuf): confiar em mirrors sem ceder verificação.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
