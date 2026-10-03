---
id: software.seguranca.tranche07.000650
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

# Radare2: Geração de Regras YARA Baseadas em Opcodes (`r2yara` / `pcy`), Exportação **SARIF** (`r2sarif`) e Gestão de Projetos

## Em uma frase
Para fechar o ciclo entre a engenharia reversa de um novo malware e a criação de assinaturas de detecção para o SOC, o Radare2 oferece comandos de impressão de padrões para YARA (**`pcy`** / plugin **`r2yara`**) e exportação padronizada de achados com **`r2sarif`**.

## Por que importa
Criar uma regra YARA copiando os bytes brutos de uma função maliciosa (`px`) costuma gerar regras frágeis que quebram na primeira recompilação porque os offsets de salto (`call 0x...`) e endereços de pilha mudam; é preciso transformar os bytes fixos da instrução em curingas (`??`) mantendo apenas os *opcodes* invariantes.

## Como funciona
No `r2`, posicionar-se no início da função exclusiva do malware e analisar os opcodes das instruções (`aoj` lista `bytes` vs `mask` de cada instrução!) permite gerar padrões hexadecimais YARA mascarados (`{ 48 89 5c 24 ?? 57 48 83 ec ?? e8 ?? ?? ?? ?? }`) resistentes a relocação de endereço.

## Exemplo
```bash
# Extrair os bytes e a mascara de relocacao (mask) das primeiras 5 instrucoes da funcao main em JSON (aoj) para regra YARA
r2 -q -A -c "s main; aoj 5" /bin/ls | jq 'map({opcode, bytes, mask})'
```

## Limites e trade-offs
Combine a máscara (`mask`) retornada por `aoj` com os `bytes` da instrução para substituir automaticamente por `??` qualquer byte onde a máscara não for `ff`, gerando uma string hexadecimal YARA imune a ASLR e relocação de linker.

## Como verificar
Valide a regra YARA gerada rodando `yr scan` sobre o binário original e sobre binários legítimos do sistema para confirmar zero falsos positivos.

## Conexões
- [[radare2-depuracao-reversivel-checkpoints-dts-rarun2-gdb-frida]] — Veja também: Radare2: Depuração Reversível (*Time-Travel Checkpoints* `dts+`/`dtsc`/`dtsr`), Perfis de Execução **`rarun2`** e Integração **`r2frida`**.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[capev2-debugger-programavel-assinaturas-yara-breakpoints-anti-sandbox]] — Referência cruzada direta com capev2-debugger-programavel-assinaturas-yara-breakpoints-anti-sandbox.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
