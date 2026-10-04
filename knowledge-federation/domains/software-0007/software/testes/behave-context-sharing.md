---
id: software.testes.tranche20.001371
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

# Behave: compartilhar estado pelo contexto

## Em uma frase
O contexto é um objeto passado a cada passo, onde valores são guardados para uso posterior dentro do mesmo cenário.

## Por que importa
O compartilhamento explícito evita variáveis globais e deixa claro em que ponto do fluxo cada dado foi produzido.

## Como funciona
Guarde o resultado produzido no passo de ação e verifique-o no passo de verificação, sem reutilizar nomes entre cenários.

## Exemplo
O identificador criado no cadastro pode ser guardado no contexto e consultado depois para confirmar a listagem.

## Limites e trade-offs
Valores deixados no contexto entre cenários contaminam execuções, e nomes genéricos escondem a origem do dado.

## Como verificar
Introduza uma falha no passo de verificação e confirme que o valor produzido pelo passo anterior está disponível como esperado.

## Conexões
- [[behave-step-definitions]] — Veja também: Behave: implementar definições de passo.
- [[behave-hooks]] — Veja também: Behave: preparar e limpar com ganchos.

## Fontes
- [Behave — Referência de API](https://behave.readthedocs.io/en/stable/api/) — funções de passo, ganchos, contexto e fixtures; consultado em 2026-10-03.
- [Behave — Tutorial](https://behave.readthedocs.io/en/stable/tutorial/) — primeiros passos, ganchos, etiquetas e fixtures; consultado em 2026-10-03.
