---
id: software.seguranca.tranche20.001915
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

# The Update Framework (TUF): Verificar hashes de targets

## Em uma frase
**The Update Framework (TUF) — Verificar hashes de targets:** Targets descreve arquivos atualizáveis com tamanho e hashes esperados para integridade do download.

## Por que importa
O recorte de **verificar hashes de targets** ajuda a proteger clientes de atualização com papéis de metadados separados, hashes, versões e limites de assinatura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificar hashes de targets**, clientes verificam Root, Timestamp, Snapshot e Targets segundo limiares, hashes, versões e expirações definidos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Compare hash do pacote baixado com metadata assinada antes de instalá-lo em sandbox. Teste em staging autorizado.

## Limites e trade-offs
Hash prova correspondência com declaração assinada, não segurança do pacote. Exceções exigem responsável e prazo.

## Como verificar
Corrompa bytes de uma cópia de teste e confirme que instalação é interrompida. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tuf-usar-snapshot-para-consistencia]] — Complementa o tópico com the update framework (tuf): usar snapshot para consistência.

## Fontes
- [TUF — Metadata](https://theupdateframework.io/docs/metadata/) — documentação oficial de papéis, metadados, assinaturas, hashes e expiração; consultado em 2026-10-04.
- [TUF — Specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md) — especificação oficial de protocolo e verificação de atualizações; consultado em 2026-10-04.
