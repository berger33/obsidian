---
id: software.seguranca.tranche07.000648
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/radareorg/radare2/master/README.md", "https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1", "https://book.rada.re/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Radare2 (`r2pipe` & QuickJS `-j`): Automação Programática de Engenharia Reversa em Python e JavaScript Nativo

## Em uma frase
A biblioteca oficial **`r2pipe`** (`radareorg/radare2-r2pipe`, disponível para Python, Go, Rust, Node.js, C# e Ruby) e o motor JavaScript **QuickJS (`qjs`)** embutido nativamente no `r2` (`r2 -j script.r2.js`) permitem automatizar qualquer tarefa de engenharia reversa comunicando-se com o `r2` através de comandos e respostas **JSON (`cmdj`)**.

## Por que importa
Em vez de fazer parsing frágil com expressões regulares sobre a saída de texto do `objdump` ou `readelf`, `r2.cmdj("aflj")`, `r2.cmdj("iIj")`, `r2.cmdj("izj")` e `r2.cmdj("pdfj")` devolvem dicionários e listas Python nativos já parseados.

## Como funciona
O método `r2pipe.open(filename, flags=["-2"])` abre o binário em processo filho silencioso, executa quantos comandos forem necessários e encerra com `r2.quit()`.

## Exemplo
```python
import r2pipe

# Abrir binario via r2pipe em Python, analisar e extrair todas as strings e suas funcoes referenciadoras
r2 = r2pipe.open("/bin/ls", flags=["-2"])
r2.cmd("aa")
info = r2.cmdj("iIj")
strings = r2.cmdj("izj")
print(f"Arquitetura: {info['arch']} {info['bits']}-bit | Total de strings na secao de dados: {len(strings)}")
r2.quit()
```

## Limites e trade-offs
Sempre feche a instância do `r2pipe` chamando **`r2.quit()`** (ou use um gerenciador de contexto) ao processar centenas de arquivos em um loop Python para evitar acumular processos `radare2` órfãos em memória.

## Como verificar
Teste executar o script Python acima e verifique que `r2.cmdj("iIj")` retorna um `dict` Python válido.

## Conexões
- [[radare2-montador-desmontador-rasm2-rax2-analise-shellcode]] — Veja também: Radare2 (`rasm2` & `rax2`): Montagem/Desmontagem Multi-Arquitetura de **Shellcodes** e Conversão de Representações Numéricas/Binárias.
- [[radare2-depuracao-reversivel-checkpoints-dts-rarun2-gdb-frida]] — Veja também: Radare2: Depuração Reversível (*Time-Travel Checkpoints* `dts+`/`dtsc`/`dtsr`), Perfis de Execução **`rarun2`** e Integração **`r2frida`**.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings]] — Referência cruzada direta com radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings.
- [[ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao]] — Referência cruzada direta com ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
