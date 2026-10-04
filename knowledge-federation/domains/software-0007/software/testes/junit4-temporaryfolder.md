---
id: software.testes.tranche23.001677
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/junit-team/junit4/wiki/Rules", "https://junit.org/junit4/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TemporaryFolder apaga sozinha — e pode cobrar prova disso

## Em uma frase
A regra TemporaryFolder cria arquivos e pastas que são deletados quando o método termina, passe ou falhe; por padrão nenhuma exceção é lançada se o recurso não puder ser apagado. O guia documenta newFile com nome, newFolder com nomes recursivos e as variantes aleatórias sem argumento.

## Por que importa
Testes de IO que escrevem no diretório de trabalho contaminam a máquina e quebram paralelismo; a regra dá a cada método um diretório virgem com limpeza garantida pelo ciclo da regra.

## Como funciona
Desde o 4.13 existe o modo estrito, opt-in via builder: TemporaryFolder.builder().assureDeletion().build() faz o teste falhar com AssertionError se os recursos não foram de fato deletados — o comportamento antigo permanece como padrão por retrocompatibilidade declarada.

## Exemplo
Troque seu @Rule new TemporaryFolder() pelo builder com assureDeletion e confirme que testes que deixam handles abertos no Windows passam a falhar na verificação de limpeza.

## Limites e trade-offs
A verificação estrita é opt-in justamente porque muitos códigos reais seguram arquivos; habilitá-la em massa produz ruído antes de virar sinal, e o guia não sugere um caminho de migração — trate como passo consciente.

## Como verificar
Abra a seção TemporaryFolder Rule da página Rules do wiki do junit4 e confirme o parágrafo de deletar ao terminar, o builder do 4.13 e a frase de retrocompatibilidade.

## Conexões
- [[junit4-timeout-two-ways]] — Veja também: Timeout por método com fork e timeout por classe com a regra.
- [[junit4-rules-collection]] — Veja também: O kit de regras: ExternalResource, ErrorCollector, Verifier, TestWatcher.

## Fontes
- [JUnit 4 — Rules (wiki)](https://github.com/junit-team/junit4/wiki/Rules) — TemporaryFolder, ExternalResource, ErrorCollector, Verifier e TestWatcher; consultado em 2026-10-03.
- [JUnit 4 — página oficial About](https://junit.org/junit4/) — modo manutenção, exemplo @Test com Hamcrest e índice de referências; consultado em 2026-10-03.
