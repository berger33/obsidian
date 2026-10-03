---
id: software.testes.tranche19.001319
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

# BackstopJS: descrever cenários

## Em uma frase
Cada cenário declara rótulo, endereço e opções que definem o estado da página no momento da captura.

## Por que importa
O cenário é a unidade de manutenção da verificação visual, e seu rótulo aparece nos relatórios e nos nomes dos arquivos.

## Como funciona
Crie um cenário por estado relevante, use rótulos descritivos e agrupe variações do mesmo componente em cenários próximos.

## Exemplo
O componente de formulário pode ter cenários de estado vazio, preenchido e com mensagem de erro.

## Limites e trade-offs
Cenários genéricos que capturam a página inteira tornam a triagem difícil, e rótulos duplicados sobrescrevem arquivos de captura.

## Como verificar
Liste os arquivos produzidos e confirme que cada cenário tem captura correspondente e identificável pelo rótulo.

## Conexões
- [[backstopjs-workflow]] — Veja também: BackstopJS: comparar capturas contra referências.
- [[backstopjs-selectors]] — Veja também: BackstopJS: limitar a captura a elementos.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — Exemplos](https://github.com/garris/BackstopJS/tree/master/examples) — configurações e cenários de exemplo; consultado em 2026-10-03.
