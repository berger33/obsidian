---
id: software.testes.tranche26.001971
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md"
fontes: ["https://raw.githubusercontent.com/YosysHQ/sby/master/README.md", "https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Licenciamento ISC e distribuição via OSS CAD Suite (gratuito) e Tabby CAD Suite

## Em uma frase
O README oficial informa que o SymbiYosys (sby) em si é licenciado sob a licença ISC (observando que os solvers e outros componentes usados por ele possuem seus próprios termos de licença) e que a maneira mais fácil de usar o sby é instalar a suíte binária — a OSS CAD Suite gratuita (github.com/YosysHQ/oss-cad-suite-build/releases) ou a Tabby CAD Suite comercial — que já contém todas as dependências necessárias, incluindo todos os solvers suportados.

## Por que importa
Compilar manualmente o Yosys e diversos solvers SMT/bit-vector em versões compatíveis costuma ser trabalhoso; baixar a OSS CAD Suite entrega o sby e todos os solvers prontos num pacote binário único, enquanto a Tabby CAD Suite adiciona suporte extensivo a SystemVerilog Assertions (SVA) e parsers industriais de SystemVerilog e VHDL.

## Como funciona
Para projetos abertos ou Verilog padrão, baixe a OSS CAD Suite em github.com/YosysHQ/oss-cad-suite-build/releases; se o projeto exigir SVA avançado ou parsers industriais de SystemVerilog e VHDL, o README orienta solicitar uma licença de avaliação da Tabby CAD Suite.

## Exemplo
Mesmo que o tutorial mencione sby e boolector como pré-requisitos, instalar a OSS CAD Suite já inclui o sby, o Yosys e o boolector na mesma árvore binária.

## Limites e trade-offs
Ao auditar licenças para uso corporativo, lembre-se da ressalva explícita do README: a licença ISC cobre o código do SymbiYosys, mas cada solver empacotado nas suítes mantém sua própria licença individual.

## Como verificar
Conferi o README oficial completo no repositório YosysHQ/sby.

## Conexões
- [[symbiyosys-what-it-is]] — Veja também: SymbiYosys (sby): driver de linha de comando para verificação formal de hardware sobre o Yosys.
- [[symbiyosys-fifo-rtl-example-structure]] — Veja também: O exemplo canônico em fifo.sv: ponteiros circulares addr_gen e banco de registradores.

## Fontes
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
