---
id: software.testes.tranche15.000869
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/docs/defaults/", "https://mswjs.io/docs/http/handling-requests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: simular erros por teste com overrides

## Em uma frase
Um teste específico pode registrar handlers de falha com `server.use()`, substituindo temporariamente o caminho feliz sem alterar a definição global.

## Por que importa
Concentrar cenários de erro nos handlers padrão obriga a recriar a suíte inteira para cada variação e esconde qual caso realmente exercita a falha.

## Como funciona
Mantenha o caminho de sucesso como padrão, registre overrides de erro no início do caso que precisa deles e deixe o reset do ciclo de vida restaurar a lista original.

## Exemplo
`server.use(http.get('/perfil', () => HttpResponse.json({ erro: 'expirado' }, { status: 401 })))` força a tela de sessão expirada apenas naquele teste.

## Limites e trade-offs
Overrides inseridos no topo podem mascarar handlers mais específicos do próprio caso, e esquecer o reset transforma o cenário de erro em estado global da suíte.

## Como verificar
Rode o caso de erro seguido do caso de sucesso e confirme que o segundo recebeu a resposta padrão, comprovando a restauração automática.

## Conexões
- [[msw-shared-handlers-across-environments]] — Veja também: MSW: compartilhar handlers entre testes, dev e Storybook.

## Fontes
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
- [MSW — Handling requests](https://mswjs.io/docs/http/handling-requests) — resposta mockada, passthrough e handlers que não respondem; consultado em 2026-10-02.
