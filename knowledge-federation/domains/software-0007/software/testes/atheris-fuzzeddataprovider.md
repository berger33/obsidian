---
id: software.testes.tranche23.001757
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://llvm.org/docs/LibFuzzer.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# FuzzedDataProvider: bytes viram tipos sem parser de fita

## Em uma frase
A página oficial documenta o equivalente Python do utilitário homônimo do libFuzzer: construído com atheris.FuzzedDataProvider(input_bytes), ele oferece uma família de Consume* que materializa a sequencia de bytes em valores — ConsumeBytes, ConsumeUnicode (com surrogate pairs possíveis, "invalid per spec but needed por ferramentas como paths no Windows", na explicação da página), ConsumeUnicodeNoSurrogates, ConsumeString (alias de Unicode no Python 3), ConsumeInt/ConsumeUInt de tamanho configurável, ConsumeIntInRange, listas com e sem range, e floats incluindo "weird values like NaN and Inf" no ConsumeFloat padrão, com ConsumeRegularFloat para os numéricos limpos.

## Por que importa
O problema que resolve é estrutural: um parser de protocolo quer (u8 comando, u32 magic, corpo), e deixar o mutador brigar com o layout dentro de um blob é desperdiçar mutações boas — o provider traduz a entropia do motor em campos tipados mantendo o fuzzing guiado por cobertura.

## Como funciona
A página lista as assinaturas completas com defaults e comportamento — por exemplo, o ConsumeInt recebendo o tamanho em bytes (two's complement, como especificado) — e o padrão espelha o FuzzedDataProvider do libFuzzer descrito na própria introdução da seção ("Similar to libFuzzer, we provide...").

## Exemplo
Converta um harness de blob único para (op = fdp.ConsumeUInt(1); payload = fdp.ConsumeBytes(4096)) e confirme que o parser agora recebe comandos válidos cedo — o caminho profundo do switch passa a ser alcançado sem acertar a mágica na posição errada do offset.

## Limites e trade-offs
A lista da seção é a superfície no snapshot — a página corta no meio da enumeração (ConsumeRegularFloat...), então quem precisa de ConsumeFloatInRange, ConsumeBool e afins deve ler o módulo completo, e a ordem dos Consumes é a ordem dos bytes: reordenar chamadas muda o mapeamento do corpus, quebrando repro de crashes velhos.

## Como verificar
Abra a subseção FuzzedDataProvider da seção API no README oficial e confirme o construtor, cada assinatura listada e as notas de surrogates, NaN e dois-complemento.

## Conexões
- [[atheris-setup-api]] — Veja também: A API de três faces: Setup, Fuzz e o internal_libfuzzer.
- [[atheris-custom-mutator]] — Veja também: Mutators custom: ensinar a gramática sem ensinar gramática.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [LLVM — libFuzzer documentation](https://llvm.org/docs/LibFuzzer.html) — motor base de cargo-fuzz e Atheris: corpus, -merge=1, requisitos do fuzz target; consultado em 2026-10-03.
