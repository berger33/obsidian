---
id: software.testes.tranche25.001891
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md", "https://diffblue.github.io/cbmc/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cobertura de padrões C89 a C23, extensões de compilador, SystemC e Verilog

## Em uma frase
O README especifica que o CBMC suporta C89, C99, a maior parte de C11, C17 e C23, além da maioria das extensões de compilador fornecidas pelo gcc e pelo Visual Studio; também suporta SystemC usando Scoot e consegue verificar consistência de programas C e C++ com outras linguagens, como Verilog.

## Por que importa
Código C/C++ industrial raramente é ISO estrito: ele usa atributos e intrínsecos do GCC ou do MSVC e, em projetos de hardware/firmware, convive com modelos SystemC ou RTL em Verilog; suportar essas extensões evita ter de reescrever o código de produção só para passar no verificador.

## Como funciona
Ao submeter código que usa extensões do gcc ou do Visual Studio ao CBMC, mantenha o ambiente de cabeçalhos compatível com o compilador alvo; para co-verificação com hardware ou modelos SystemC, consulte a documentação do CProver sobre Scoot e equivalência com Verilog.

## Exemplo
Um módulo de firmware em C17 com extensões do GCC pode ser analisado diretamente pelo frontend do CBMC sem remover atributos específicos do compilador.

## Limites e trade-offs
O texto oficial diz "most of C11, C17, C23 and most compiler extensions": construções exóticas fora desse subconjunto ainda podem requerer adaptação ou consulta às notas da versão.

## Como verificar
Conferi a lista de padrões e linguagens na seção About do README oficial.

## Conexões
- [[cbmc-what-it-is]] — Veja também: CBMC: Bounded Model Checker para programas C e C++.
- [[cbmc-verified-properties-and-unwinding]] — Veja também: O que e como verifica: bounds, ponteiros, exceções, asserções e loop unwinding.

## Fontes
- [CBMC — README oficial](https://raw.githubusercontent.com/diffblue/cbmc/develop/README.md) — README oficial do CBMC com suporte a C89–C23, extensões gcc/Visual Studio, SystemC/Scoot, Verilog, loop unwinding, canais release vs develop, instalação em Windows/Linux/macOS, contribuição e licença 4-clause BSD.; consultado em 2026-10-03.
- [CProver & CBMC Documentation oficial](https://diffblue.github.io/cbmc/) — Documentação oficial da suíte CProver e do verificador CBMC.; consultado em 2026-10-03.
