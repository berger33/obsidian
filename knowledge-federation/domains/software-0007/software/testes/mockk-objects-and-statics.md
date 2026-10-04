---
id: software.testes.tranche20.001424
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: dublar objetos e membros estáticos

## Em uma frase
A biblioteca cobre objetos únicos, métodos estáticos, funções de nível superior, extensões e construtores, com limpeza explícita ao final.

## Por que importa
Muitos códigos Kotlin dependem de objetos únicos e extensões, que os dublês tradicionais não alcançam.

## Como funciona
Duble o objeto ou membro estático apenas quando o código depender dele, e sempre desfaça a transformação ao terminar o caso.

## Exemplo
Um objeto de configuração global pode ser dublado para devolver o valor do caso e restaurado ao final da execução.

## Limites e trade-offs
Não restaurar o objeto deixa o dublê ativo para casos seguintes, e dublar membros muito centrais esconde o acoplamento em vez de expô-lo.

## Como verificar
Duble um objeto, execute o caso e verifique que a transformação é desfeita, rodando outro caso que usa o objeto real.

## Conexões
- [[mockk-coroutines]] — Veja também: MockK: dublar funções suspensas.
- [[mockk-configuration]] — Veja também: MockK: configurar o comportamento padrão do projeto.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
