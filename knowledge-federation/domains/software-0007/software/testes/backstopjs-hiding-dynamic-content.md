---
id: software.testes.tranche19.001323
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/garris/BackstopJS/blob/master/README.md", "https://github.com/garris/BackstopJS/tree/master/examples"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# BackstopJS: isolar conteúdo dinâmico

## Em uma frase
O cenário pode ocultar ou remover seletores antes da captura, eliminando do quadro relógios, avisos e dados que mudam a cada acesso.

## Por que importa
Isolar o que varia é o que torna a comparação visual estável sem desligar a verificação.

## Como funciona
Oculte com preservação de espaço quando o layout importa, remova quando não importa e documente cada exclusão.

## Exemplo
A faixa de aviso de cookies pode ser removida, e o campo de data atual ocultado mantendo o espaço reservado.

## Limites e trade-offs
Ocultar demais reduz a cobertura a ponto de a verificação não flagrar mudanças reais, e remover elementos altera o layout de forma que a referência pode divergir do uso real.

## Como verificar
Compare uma captura com e sem o conteúdo dinâmico oculto e confirme que a diferença entre execuções desaparece.

## Conexões
- [[backstopjs-mismatch-threshold]] — Veja também: BackstopJS: ajustar a tolerância de diferença.
- [[backstopjs-viewports]] — Veja também: BackstopJS: cobrir tamanhos de tela.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — Exemplos](https://github.com/garris/BackstopJS/tree/master/examples) — configurações e cenários de exemplo; consultado em 2026-10-03.
