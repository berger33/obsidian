---
id: software.testes.tranche24.001856
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

# Record and Playback: gravar o backend real para replay

## Em uma frase
Entre as Features listadas na página da crate está "Record and Playback", e a API correspondente aparece nos itens documentados: Recording, "a recording of interactions (requests and responses) on a mock server... used to capture and store detailed information about the HTTP requests received by the server and the corresponding responses sent back", com RecordingRuleBuilder para configurar o que é capturado.

## Por que importa
O modo muda de categoria o teste de integração contra serviço de terceiro: grava-se a conversa real uma vez (conforme as regras), e o replay devolve a resposta histórica — determinístico para CI, sem chave de API viva nem latência de rede, e ainda fiel ao formato real do provedor.

## Como funciona
Configure a gravação via RecordingRuleBuilder num servidor que encaminha ao upstream real, rode a sessão de gravação uma vez (em ambiente autorizado), versione os artefatos e rode os testes seguintes contra o playback — o mesmo servidor MockServer serve os dois papéis.

## Exemplo
O par de capacidades (forward/proxy + record) aparece junto na lista de features: o encaminhamento é o que permite ao servidor ver o tráfego real durante a gravação.

## Limites e trade-offs
Os formatos de persistência e a API detalhada de gravação não constam da página da crate além da lista e dos itens; os exemplos do diretório de testes da crate e o site oficial são o caminho declarado para o uso fino.

## Como verificar
A feature "Record and Playback" e o struct Recording estão na página oficial no docs.rs.

## Conexões
- [[httpmock-mock-lifecycle]] — Veja também: O handle Mock: observar contagens e remover mocks.
- [[httpmock-forward-proxy]] — Veja também: Forward e Proxy mode: o mock que sabe encaminhar.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
