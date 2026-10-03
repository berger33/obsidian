---
id: software.seguranca.tranche07.000636
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

# Ghidra: Reconhecimento de Bibliotecas Estáticas com **FunctionID (`fidb`)** e Busca Vetorial de Similaridade Comportamental com **BSim**

## Em uma frase
Quando um binário de malware ou firmware IoT é compilado estaticamente (`static linking` com `libc`, `OpenSSL`, `mbedTLS`, `zlib` ou `libcurl`), mais de 90% das 15.000 funções presentes no executável são apenas código de biblioteca padrão sem símbolos; o Ghidra resolve esse problema com dois motores complementares: **FunctionID (`fidb`)** e **BSim (*Behavioral Similarity*)**.

## Por que importa
O **FunctionID** calcula hashes precisos das instruções (mascarando endereços relocáveis) e os compara contra bancos `.fidb` de bibliotecas conhecidas para renomear instantaneamente milhares de funções de biblioteca; porém, se a biblioteca ou malware foi compilado com outro compilador, flags de otimização (`-O2` vs `-Os`) ou para outra arquitetura de CPU, os bytes mudam.

## Como funciona
É aí que entra o **BSim** (integrado ao Ghidra): ele extrai vetores de características semânticas do **fluxo de dados e controle P-Code descompilado** de cada função e os indexa em um banco vetorial (H2 local, Elasticsearch ou PostgreSQL com extensão BSim), encontrando funções equivalentes mesmo quando compiladas para arquiteturas ou níveis de otimização diferentes.

## Exemplo
```bash
# Gerar assinaturas BSim em lote a partir de binarios de referencia usando o utilitario headless bsim
/opt/ghidra/support/bsim generatesigs \
  ghidra:/cases/ghidra-projects/MalwareTriageProj \
  /cases/bsim-xmls/
```

## Limites e trade-offs
Use **FunctionID (`fidb`)** primeiro para rotular rapidamente bibliotecas estáticas exatas do mesmo compilador/arquitetura, e em seguida use **BSim** para comparar amostras novas de malware contra o repositório histórico de famílias já analisadas pelo seu CSIRT.

## Como verificar
Ative o painel *BSim Search* no Ghidra sobre uma função de criptografia desconhecida e verifique os matches ordenados por pontuação de similaridade e significância estatística (`confidence`).

## Conexões
- [[ghidra-reconstrucao-tipos-structs-classes-cpp-rtti-vtables-pdb-dwarf]] — Veja também: Ghidra: Reconstrução de Estruturas C (`Data Type Manager`), Classes C++ (`RTTI` / `vtable`), *Parse C Source* e Símbolos **PDB / DWARF**.
- [[ghidra-engenharia-reversa-firmware-bare-metal-memory-map-svd]] — Veja também: Ghidra: Engenharia Reversa de **Firmware Embarcado / Bare-Metal** (Descoberta de *Base Address*, *Memory Map* MMIO e Arquivos CMSIS **SVD**).
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.
- [[ghidra-representacao-intermediaria-pcode-analise-fluxo-dados-varnodes]] — Referência cruzada direta com ghidra-representacao-intermediaria-pcode-analise-fluxo-dados-varnodes.
- [[radare2-comparacao-binarios-patch-diffing-radiff2-assinaturas-zignatures]] — Referência cruzada direta com radare2-comparacao-binarios-patch-diffing-radiff2-assinaturas-zignatures.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
