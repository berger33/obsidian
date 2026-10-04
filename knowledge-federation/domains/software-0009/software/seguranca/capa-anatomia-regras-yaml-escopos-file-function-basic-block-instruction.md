---
id: software.seguranca.tranche13.001223
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/capa/master/README.md", "https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia das Regras YAML do **`capa-rules`**: Escopos Estáticos (**`file`, `function`, `basic block`, `instruction`**) e Operadores Lógicos (`and`, `or`, `count`, `optional`)

## Em uma frase
Como escrever uma regra customizada para o `capa` capaz de detectar uma técnica proprietária de um grupo APT sem depender de hashes ou strings facilmente alteráveis pelo atacante?

## Por que importa
Toda regra do repositório oficial **`mandiant/capa-rules`** é um documento YAML composto por dois blocos: **`meta`** (que define `name`, `namespace`, mapeamentos `att&ck` e `mbc`, `authors`, `examples` e, crucialmente, o **`scope`**!) e **`features`** (a árvore lógica de características de código que devem ser satisfeitas dentro daquele escopo)!

## Como funciona
No `capa` para análise estática, existem **4 escopos hierárquicos (`scope`)**: **(1) `instruction`** (avalia características dentro de uma única instrução assembly, ex.: `mnemonic: xor` com operandos específicos); **(2) `basic block`** (avalia instruções dentro do mesmo bloco básico sem desvios de salto); **(3) `function`** (o escopo mais utilizado: avalia chamadas de API, números, strings, loops `characteristic: tight loop` e sub-regras `match` dentro da mesma função!); e **(4) `file`** (avalia características globais do binário inteiro, como nomes de seções PE, imports, exports e combinação de múltiplas regras de função)!

## Exemplo
```yaml
# Exemplo de regra YAML customizada do capa no escopo 'function' para detectar injecao de codigo classica em processo remoto
rule:
  meta:
    name: inject thread into remote process via VirtualAllocEx
    namespace: host-interaction/process/inject
    att&ck:
      - Defense Evasion::Process Injection [T1055]
    mbc:
      - Process::Inject Code [C0037]
    scopes:
      static: function
      dynamic: span of calls
    examples:
      - 9324d1a8ae37a36ae560c37448c9705a:0x401520
  features:
    - and:
      - api: OpenProcess
      - api: VirtualAllocEx
      - api: WriteProcessMemory
      - or:
        - api: CreateRemoteThread
        - api: NtCreateThreadEx
```

## Limites e trade-offs
Repare no campo **`scopes: static: function`** e **`dynamic: span of calls`** da regra acima: uma única regra YAML do `capa` pode detectar a técnica tanto estaticamente (olhando para os imports/calls dentro de uma função desmontada) quanto dinamicamente (olhando para uma janela sequencial de chamadas de API registradas por uma sandbox)!

## Como verificar
Use o linter e testador oficial do repositório `capa-rules` para validar sintaxe e performance de novas regras antes de adicioná-las ao seu diretório `-r ./minhas_regras_capa/`.

## Conexões
- [[capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao]] — Veja também: Triagem Rápida vs. Engenharia Reversa Profunda no `capa`: Modos Padrão, Verboso (**`-v`**), Muito Verboso (**`-vv`**) e Exportação **`-j` JSON**.
- [[capa-filtros-restricao-escopo-tags-functions-processes-otimizacao]] — Veja também: Acelerando o `capa` em Binários Complexos: Filtros por Tag/Namespace (**`-t`**), Restrição por Endereço de Função (**`--restrict-to-functions`**) e Cache **`.viv`**.
- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Referência cruzada direta com capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant.

## Fontes
- [Mandiant FLARE `capa` Official GitHub — Detect Capabilities in Executable Files](https://raw.githubusercontent.com/mandiant/capa/master/README.md) — repositório oficial do Mandiant `capa` cobrindo identificação de capacidades em PE, ELF, .NET, shellcode e relatórios de sandbox mapeadas ao ATT&CK e MBC; consultado em 2026-10-03.
- [Mandiant `capa` Official Usage & Advanced Documentation (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/capa/master/doc/usage.md) — guia técnico oficial de uso do `capa` detalhando modos `-v`/`-vv`/`-j`, filtros `-t`, `--restrict-to-functions`, `--restrict-to-processes`, `CAPA_SAVE_WORKSPACE` e integrações IDA/Ghidra/Web; consultado em 2026-10-03.
