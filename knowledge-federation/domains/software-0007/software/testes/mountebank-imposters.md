---
id: software.testes.tranche19.001278
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
fontes: ["https://www.mbtest.org/docs/api/overview", "https://github.com/bbyars/mountebank"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: criar serviços virtuais com impostores

## Em uma frase
Um impostor é um serviço virtual que escuta em uma porta e fala um protocolo, definido por porta, protocolo e lista de stubs.

## Por que importa
Os impostores ficam entre a aplicação e as dependências externas, permitindo testar fluxos que dependeriam de serviços indisponíveis ou caros.

## Como funciona
Defina o impostor com porta e protocolo, descreva os stubs e crie-o pela interface administrativa ou por arquivo de configuração.

## Exemplo
Uma cobrança pode apontar o cliente para um impostor local que devolve a resposta do provedor de pagamento durante o teste.

## Limites e trade-offs
Portas fixas colidem entre execuções paralelas, e impostores esquecidos ativos interferem nas execuções seguintes.

## Como verificar
Crie o impostor, consulte seu estado pela interface e remova-o ao final, confirmando que a porta foi liberada.

## Conexões
- [[mountebank-stubs]] — Veja também: Mountebank: compor stubs com respostas.

## Fontes
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
- [Mountebank — repositório oficial](https://github.com/bbyars/mountebank) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
