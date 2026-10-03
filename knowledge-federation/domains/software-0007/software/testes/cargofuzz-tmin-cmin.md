---
id: software.testes.tranche23.001707
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
fontes: ["https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md", "https://llvm.org/docs/LibFuzzer.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minificação local e global: tmin para um caso, cmin para o corpus

## Em uma frase
O README define os dois redutores de forma simétrica: cargo fuzz tmin <target> <input> — "Found a failing input? Minify it to the smallest input that causes that failure" — e cargo fuzz cmin <target>, que minifica o corpus de arquivos de input inteiro, descartando os que não pagam seu aluguel na cobertura.

## Por que importa
tmin é o primeiro socorro de qualquer crash: o input do libFuzzer pode ser dezenas de kilobytes com dois bytes relevantes, e a redução automática mantém o mesmo caminho de falha com uma fração do payload — é o pré-requisito para um teste de regressão legível.

## Como funciona
Os dois são pós-processamento sobre o material existente (arquivos em fuzz/artifacts e fuzz/corpus), o que espelha as ferramentas de mesma função no AFL++ (afl-tmin e afl-cmin) — ecossistemas distintos, mesma disciplina documentada nos READMEs oficiais de ambos.

## Exemplo
Pegue o maior arquivo de crash da sua última campanha, rode tmin e confira o tamanho resultante e que a falha continua reproduzível; em seguida, rode cmin no corpus e compare a listagem antes/depois.

## Limites e trade-offs
O README documenta a intenção, não o custo: minificação roda o alvo milhares de vezes em busca do mínimo — tempo proporcional ao input — e os knobs finos (como limites e tempo) ficam no --help, sem contrato estável entre versões.

## Como verificar
Abra as seções tmin e cmin do README oficial do cargo-fuzz e confirme as duas frases de definição na íntegra.

## Conexões
- [[cargofuzz-fmt-arbitrary]] — Veja também: cargo fuzz fmt: o que aquele input arbitrário realmente é.
- [[cargofuzz-coverage-docs]] — Veja também: cargo fuzz coverage e onde a documentação real mora.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [LLVM — libFuzzer documentation](https://llvm.org/docs/LibFuzzer.html) — motor base de cargo-fuzz e Atheris: corpus, -merge=1, requisitos do fuzz target; consultado em 2026-10-03.
