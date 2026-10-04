---
id: software.seguranca.tranche20.001917
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

# The Update Framework (TUF): Delegar Targets por escopo

## Em uma frase
**The Update Framework (TUF) — Delegar Targets por escopo:** Delegações permitem particionar nomes de targets e chaves entre equipes ou repositórios.

## Por que importa
O recorte de **delegar targets por escopo** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **delegar targets por escopo**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Delegue prefixo de pacote de teste a chave de equipe com escopo restrito. Teste em staging autorizado.

## Limites e trade-offs
Delegação ampla pode conceder controle de targets de outra equipe. Exceções exigem responsável e prazo.

## Como verificar
Tente publicar target fora do prefixo e confirme que assinatura não autoriza o caminho. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-rotacionar-chave-root-com-cuidado]] — Complementa o tópico com the update framework (tuf): rotacionar chave root com cuidado.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
