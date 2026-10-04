---
id: software.testes.tranche17.001124
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://wiremock.org/docs/standalone/java-jar/", "https://github.com/wiremock/wiremock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WireMock: executar de forma autônoma no pipeline

## Em uma frase
O servidor pode rodar como processo independente ou contêiner, aceitando diretório de stubs e porta por argumento de linha de comando.

## Por que importa
Subir o simulador como processo separado mantém o teste independente da linguagem e permite reutilizar o mesmo conjunto de stubs.

## Como funciona
Inicie com o diretório de stubs versionado, defina porta fixa para o pipeline e derrube o processo ao final da execução.

## Exemplo
Um trabalho de integração pode subir o contêiner do simulador, rodar a suíte e encerrar o processo, publicando o log de chamadas como artefato.

## Limites e trade-offs
Portas ocupadas e processos remanescentes causam falhas intermitentes, e o diretório de stubs precisa ser montado no caminho correto.

## Como verificar
Suba o processo, consulte a rota de saúde e confirme a ordem de encerramento no log ao final da execução.

## Conexões
- [[wiremock-record-playback]] — Veja também: WireMock: gravar tráfego e reproduzir.
- [[wiremock-limits-and-practices]] — Veja também: WireMock: reconhecer limites da simulação.

## Fontes
- [WireMock — Standalone](https://wiremock.org/docs/standalone/java-jar/) — execução autônoma, argumentos de linha de comando e contêiner; consultado em 2026-10-03.
- [WireMock — repositório oficial](https://github.com/wiremock/wiremock) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
