---
id: software.testes.tranche24.001857
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://docs.rs/httpmock/latest/httpmock/", "https://github.com/httpmock/httpmock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Forward e Proxy mode: o mock que sabe encaminhar

## Em uma frase
As Features listam "Forward and Proxy Mode", e a API documenta as peças: ForwardingRule — "represents a forwarding rule on a MockServer, allowing HTTP requests that meet specific criteria to be redirected to a designated destination. Each rule is uniquely identified by an ID within the server context" — mais ProxyRule e seus builders (ForwardingRuleBuilder, ProxyRuleBuilder).

## Por que importa
A utilidade não é só para teste: um servidor que decide por critério o que responder localmente e o que encaminhar ao real é o dispositivo de testes híbridos — half mock, half proxy — e também a base de gravação/replay e de inspeção de tráfego em ambientes de QA.

## Como funciona
Defina as regras com os builders, referencie cada regra pelo ID único no contexto do servidor (a doc do struct afirma a identidade por ID), e aponte o cliente para o servidor httpmock em vez do real — o que não for mockado segue por encaminhamento.

## Exemplo
Cenário de fuzzer de contrato: mockar apenas os endpoints ainda não implementados e deixar o resto fluir para o backend de staging via forwarding rule no mesmo servidor.

## Limites e trade-offs
Os critérios exatos de match das regras e as diferenças semânticas entre forward e proxy modes não estão detalhados na página da crate; a doc dos structs e o site oficial cobrem o comportamento fino.

## Como verificar
A linha de features e os itens ForwardingRule/ProxyRule da documentação de API sustentam a nota.

## Conexões
- [[httpmock-record-playback]] — Veja também: Record and Playback: gravar o backend real para replay.
- [[httpmock-standalone-yaml]] — Veja também: Standalone mode com Docker e mocks em YAML.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
