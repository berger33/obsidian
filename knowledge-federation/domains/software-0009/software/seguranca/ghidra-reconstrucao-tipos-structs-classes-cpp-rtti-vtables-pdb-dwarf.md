---
id: software.seguranca.tranche07.000635
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
fontes: ["https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md", "https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md", "https://github.com/NationalSecurityAgency/ghidra/security/advisories"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ghidra: Reconstrução de Estruturas C (`Data Type Manager`), Classes C++ (`RTTI` / `vtable`), *Parse C Source* e Símbolos **PDB / DWARF**

## Em uma frase
A diferença entre uma saída de descompilador ilegível cheia de aritmética de ponteiros brutos (`*(int *)(param_1 + 0x28) = 1;`) e um código C cristalino (`ctx->is_authenticated = 1;`) no Ghidra está na aplicação de **estruturas, tipos de dados e símbolos** no **`Data Type Manager`**.

## Por que importa
Em binários compilados em C/C++, Rust ou Go onde os símbolos foram removidos (`stripped`), definir a assinatura correta das funções (`F` / *Edit Function Signature*) e criar ou importar cabeçalhos `.h` (*File -> Parse C Source...*) faz o motor de propagação de tipos do descompilador atualizar automaticamente todas as variáveis dependentes.

## Como funciona
Para binários C++, o analisador nativo de **RTTI (*Run-Time Type Information*)** e os scripts de reconstrução de **`vtable`** (tabelas de métodos virtuais) identificam a hierarquia de herança de classes, enquanto para binários com símbolos disponíveis o Ghidra carrega automaticamente informações **DWARF** (ELF) e arquivos **Microsoft PDB** (`File -> Load PDB File...`).

## Exemplo
```c
/* Exemplo de cabecalho C importavel no Ghidra via File -> Parse C Source para tipar a configuracao de um implant */
#pragma pack(push, 1)
typedef struct _IMPLANT_CONFIG {
    unsigned int magic_header;
    unsigned int sleep_seconds;
    unsigned short jitter_percent;
    unsigned short c2_port;
    char c2_domain[64];
    unsigned char aes_key[32];
} IMPLANT_CONFIG, *PIMPLANT_CONFIG;
#pragma pack(pop)
```

## Limites e trade-offs
No atalho **`T`** (*Choose Data Type*) ou **`Ctrl+L`** (*Retype Variable*) dentro da janela do Descompilador, quando você encontra uma alocação `ptr = malloc(0x6c);`, clicar com o botão direito sobre `ptr` e escolher **`Auto Create Structure`** cria automaticamente o esqueleto da `struct` preenchido com todos os offsets acessados pela função!

## Como verificar
Aplique `IMPLANT_CONFIG *` ao parâmetro da função de inicialização no Descompilador e verifique que todos os acessos `param_1 + offset` são substituídos pelos nomes dos campos.

## Conexões
- [[ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao]] — Veja também: Ghidra: Desenvolvimento de Scripts em **Python 3 Nativo (`PyGhidra`)** e Uso da **`FlatProgramAPI`**.
- [[ghidra-identificacao-funcoes-estaticas-functionid-fidb-bsim]] — Veja também: Ghidra: Reconhecimento de Bibliotecas Estáticas com **FunctionID (`fidb`)** e Busca Vetorial de Similaridade Comportamental com **BSim**.
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.
- [[volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map]] — Referência cruzada direta com volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
