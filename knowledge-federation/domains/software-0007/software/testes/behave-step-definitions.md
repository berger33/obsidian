---
id: software.testes.tranche20.001370
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://behave.readthedocs.io/en/stable/api/", "https://behave.readthedocs.io/en/stable/tutorial/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Behave: implementar definições de passo

## Em uma frase
Funções decoradas associam cada passo do texto a código Python, com parâmetros capturados por expressões no padrão do passo.

## Por que importa
A associação por texto mantém o vocabulário do negócio como contrato e permite reaproveitar o mesmo passo em várias funcionalidades.

## Como funciona
Mantenha definições curtas, capture valores por nomes descritivos e prefira passos de domínio a passos genéricos de clique.

## Exemplo
O passo de adicionar produto ao carrinho pode receber a quantidade como parâmetro e delegar a ação ao objeto de página.

## Limites e trade-offs
Passos genéricos demais viram uma linguagem paralela ao negócio, e parâmetros sem tipo geram falhas de conversão difíceis de ler.

## Como verificar
Execute a suíte com um passo ainda não implementado e use o esqueleto sugerido pelo próprio relatório para implementá-lo.

## Conexões
- [[behave-feature-files]] — Veja também: Behave: escrever arquivos de funcionalidade.
- [[behave-context-sharing]] — Veja também: Behave: compartilhar estado pelo contexto.

## Fontes
- [Behave — Referência de API](https://behave.readthedocs.io/en/stable/api/) — funções de passo, ganchos, contexto e fixtures; consultado em 2026-10-03.
- [Behave — Tutorial](https://behave.readthedocs.io/en/stable/tutorial/) — primeiros passos, ganchos, etiquetas e fixtures; consultado em 2026-10-03.
