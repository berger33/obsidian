---
id: software.seguranca.tranche07.000645
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

# Radare2 (`radiff2` & Zignatures `z`): *Patch Diffing* de Binários (`-g`, `-AC`) e Reconhecimento de Funções com **Zignatures**

## Em uma frase
O utilitário **`radiff2`** compara dois arquivos binários para encontrar diferenças no nível de bytes, strings, funções e grafos de fluxo de controle (*Binary Patch Diffing*), enquanto o subsistema de **Zignatures (`z`)** do `r2` gera e aplica assinaturas de funções para identificar código reutilizado em binários *stripped*.

## Por que importa
Quando uma biblioteca recebe uma atualização de segurança, rodar `radiff2 -AC lib_vuln.so lib_patched.so` faz o matching de todas as funções entre os dois binários listando o índice de similaridade (`0.0` a `1.0` + `MATCH` / `UNMATCH` / `NEW`), e **`radiff2 -g <funcao> lib_vuln.so lib_patched.so | xdot -`** gera o grafo visual Graphviz destacando exatamente os blocos básicos adicionados ou modificados pelo patch.

## Como funciona
Já os comandos **`zg`** (*generate zignatures*), **`zos <arquivo.sdb>`** (salva o banco de assinaturas) e **`zo <arquivo.sdb>`** (aplica assinaturas em um binário sem símbolos) permitem reconhecer funções de bibliotecas estáticas ou variantes da mesma família de malware.

## Exemplo
```bash
# Comparar duas versoes de um binario ao nivel de funcoes (-AC) filtrando apenas funcoes modificadas (UNMATCH)
radiff2 -AC /cases/patches/target_v1.bin /cases/patches/target_v2.bin | grep -v "1.000000"
```

## Limites e trade-offs
Para gerar o grafo de diferenças em formato **Mermaid** ou **Graphviz DOT** a partir do `radiff2`, combine `-g <simbolo_ou_offset> -m d` (DOT) ou `-m j` (JSON) para incluir diretamente no relatório técnico da vulnerabilidade.

## Como verificar
Teste `radiff2 -s arquivo1 arquivo2` para calcular rapidamente a distância de similaridade global entre duas amostras de malware.

## Conexões
- [[radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao]] — Veja também: Radare2: Emulação Segura com **ESIL (*Evaluable Strings Intermediate Language*)** (`aei`, `aeim`, `aes`, `aeso` e `emu.str=true`).
- [[radare2-busca-padroes-rafind2-rahash2-entropia-secoes-empacotamento]] — Veja também: Radare2 (`rafind2` & `rahash2`): Caça de Padrões Binários/ROP Gadgets e Cálculo de **Entropia por Blocos** para Detecção de *Packers* e Chaves.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[ghidra-colaboracao-ghidraserver-version-tracking-patch-diffing]] — Referência cruzada direta com ghidra-colaboracao-ghidraserver-version-tracking-patch-diffing.
- [[ghidra-identificacao-funcoes-estaticas-functionid-fidb-bsim]] — Referência cruzada direta com ghidra-identificacao-funcoes-estaticas-functionid-fidb-bsim.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
